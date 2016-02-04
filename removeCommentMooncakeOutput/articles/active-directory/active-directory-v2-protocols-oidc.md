
<properties
	pageTitle="App Model v2.0 OpenID Connect Protocol | Windows Azure"
	description="Building web sites using Azure AD's implementation of the OpenID Connect authentication protocol."
	services="active-directory"
	documentationCenter=""
	authors="dstrockis"
	manager="msmbaldwin"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="12/09/2015"
	wacn.date=""/>

# App model v2.0 preview: Protocols - OpenID Connect
OpenID Connect is an authentication protocol built on top of OAuth 2.0 that can be used to securely sign users into web sites.  Using the app model v2.0's implementation of OpenID Connect, you can add sign in and API access to your web based applications.  This guide will show you how to do so in a language-independent manner, describing how to send and receive HTTP messages without using any of our open-source libraries.

> [AZURE.NOTE]
	This information applies to the v2.0 app model public preview.  For instructions on how to integrate with the generally available Azure AD service, please refer to the [Azure Active Directory Developer Guide](/documentation/articles/active-directory-developers-guide).

[OpenID Connect](http://openid.net/specs/openid-connect-core-1_0.html) extends the OAuth 2.0 *authorization* protocol for use as an *authentication* protocol, which allows you to perform single sign-on using OAuth.  It introduces the concept of an `id_token`, which is a security token that allows the client to verify the identity of the user and obtain basic profile information about the user.  Because it extends OAuth 2.0, it also enables apps to securely acquire **access_tokens** which can be used to access resources that are secured by an [authorization server](/documentation/articles/active-directory-v2-protocols#the-basics).  OpenID Connect is our recommendation if you are building a [web site](/documentation/articles/active-directory-v2-flows#web-apps) that is hosted on a server and accessed via a browser.

## Send the Sign-In Request
When your web site needs to authenticate the user, it can direct the user to the `/authorize` endpoint.  This request is similar to the first leg of the [OAuth 2.0 Authorization Code Flow](/documentation/articles/active-directory-v2-protocols-oauth-code), with a few important distinctions:

- The request must include the scope `openid` in the `scope` parameter.
- The `response_type` parameter must include `id_token`
- The request must include the `nonce` parameter

```
// Line breaks for legibility only

GET https://login.chinacloudapi.cn/common/oauth2/v2.0/authorize?
client_id=2d4d11a2-f814-46a7-890a-274a72a7309e		// Your registered Application Id
&response_type=id_token
&redirect_uri=http%3A%2F%2Flocalhost%2Fmyapp%2F 	  // Your registered Redirect Uri, url encoded
&response_mode=query							      // 'query', 'form_post', or 'fragment'
&scope=openid										 // Translates to the 'Read your profile' permission
&state=12345						 				 // Any value, provided by your app
&nonce=678910										 // Any value, provided by your app
```

| Parameter | | Description |
| ----------------------- | ------------------------------- | --------------- |
| client_id | required | The Application Id that the registration portal ([apps.dev.microsoft.com](https://apps.dev.microsoft.com)) assigned your app. |
| response_type | required | Must include `id_token` for OpenID Connect sign-in.  It may also include other response_types, such as `code`. |
| redirect_uri | required | The redirect_uri of your app, where authentication responses can be sent and received by your app.  It must exactly match one of the redirect_uris you registered in the portal, except it must be url encoded. |
| scope | required | A space-separated list of scopes.  For OpenID Connect, it must include the scope `openid`, which translates to the "Sign in & Read Your Profile" permission in the consent UI.  You may also include other scopes in this request for requesting consent.  |
| nonce | required | A value included in the request, generated by the app, that will be included in the resulting id_token as a claim.  The app can then verify this value to mitigate token replay attacks.  The value is typically a randomized, unique string that can be used to identify the origin of the request.  |
| response_mode | recommended | Specifies the method that should be used to send the resulting authorization_code back to your app.  Can be one of 'query', 'form_post', or 'fragment'.  
| state | recommended | A value included in the request that will also be returned in the token response.  It can be a string of any content that you wish.  A randomly generated unique value is typically used for preventing cross-site request forgery attacks.  The state is also used to encode information about the user's state in the app before the authentication request occurred, such as the page or view they were on. |
| prompt | optional | Indicates the type of user interaction that is required.  The only valid values at this time are 'login', 'none', and 'consent'.  `prompt=login` will force the user to enter their credentials on that request, negating single-sign on.  `prompt=none` is the opposite - it will ensure that the user is not presented with any interactive prompt whatsoever.  If the request cannot be completed silently via single-sign on, the v2.0 endpoint will return an error.  `prompt=consent` will trigger the OAuth consent dialog after the user signs in, asking the user to grant permissions to the app. |
| login_hint | optional | Can be used to pre-fill the username/email address field of the sign in page for the user. |

At this point, the user will be asked to enter their credentials and complete the authentication.  The v2.0 endpoint will also ensure that the user has consented to the permissions indicated in the `scope` query parameter.  If the user has not consented to any of those permissions, it will ask the user to consent to the required permissions.  Details of [permissions, consent, and multi-tenant apps are provided here](/documentation/articles/active-directory-v2-scopes).

Once the user authenticates and grants consent, the v2.0 endpoint will return a response to your app at the indicated `redirect_uri`, using the method specified in the `response_mode` parameter.

A successful response using `response_mode=query` looks like:

```
GET https://localhost/myapp/?
id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik5HVEZ2ZEstZnl0aEV1Q... 	// the id_token, truncated
&session_state=7B29111D-C220-4263-99AB-6F6E135D75EF			   // a value generated by the v2.0 endpoint
&state=12345												  	// the value provided in the request
&id_token_expires_in=3600

```

| Parameter | Description |
| ----------------------- | ------------------------------- |
| id_token | The id_token that the  app requested. You can use the id_token to verify the user's identity and begin a session with the user.  More details on id_tokens and their contents is included in the [v2.0 endpoint token reference](/documentation/articles/active-directory-v2-tokens).  |
| session_state | A unique value that identifies the current user session. This value is a GUID, but should be treated as an opaque value that is passed without examination. |
| state | If a state parameter is included in the request, the same value should appear in the response. The  app should verify that the state values in the request and response are identical. |
| id_token_expires_in | How long the id token is valid (in seconds). |


Error responses may also be sent to the `redirect_uri` so the app can handle them appropriately:

```
GET https://localhost/myapp/?
error=access_denied
&error_description=the+user+canceled+the+authentication
```

| Parameter | Description |
| ----------------------- | ------------------------------- |
| error | An error code string that can be used to classify types of errors that occur, and can be used to react to errors. |
| error_description | A specific error message that can help a developer identify the root cause of an authentication error.  |

## Validate the id_token
Just receiving an id_token is not sufficient to authenticate the user; you must validate the id_token's signature and verify the claims in the token per your  app's requirements.  The v2.0 endpoint uses [JSON Web Tokens (JWTs)](http://self-issued.info/docs/draft-ietf-oauth-json-web-token.html) and public key cryptography to sign tokens and verify that they are valid.

The v2.0 app model has an OpenID Connect metadata endpoint, which allows an app to fetch information about the v2.0 app model at runtime.  This information includes endpoints, token contents, and token signing keys.  The metadata endpoint contains a JSON document located at:

`https://login.chinacloudapi.cn/common/v2.0/.well-known/openid-configuration`

One of the properties of this configuration document is the `jwks_uri`, whose value for the v2.0 app model will be:

`https://login.chinacloudapi.cn/common/discovery/v2.0/keys`.

You can use the RSA256 public keys located at this endpoint to validate the signature of the id_token.  There are multiple keys listed at this endpoint at any given point in time, each identified by a `kid`.  The header of the id_token also contains a `kid` claim, which indicates which of these keys was used to sign the id_token.  

See the [v2.0 app model token reference](/documentation/articles/active-directory-v2-tokens) for more information, including [Validating Tokens](/documentation/articles/active-directory-v2-tokens#validating-tokens) and [Important Information About Signing Key Rollover](/documentation/articles/active-directory-v2-tokens#validating-tokens).
<!--TODO: Improve the information on this-->

Once you've validated the signature of the id_token, there are a few claims you will need to verify:

- You should validate the `nonce` claim to prevent token replay attacks.  Its value should be what you specified in the sign-in request.
- You should validate the `aud` claim to ensure the id_token was issued for your app.  Its value should be the `client_id` of your app.
- You should validate the `iat` and `exp` claims to ensure the id_token has not expired.

You may also wish to validate additional claims depending on your scenario.  Some common validations include:

- Ensuring the user/organization has signed up for the  app.
- Ensuring the user has proper authorization/privileges
- Ensuring a certain strength of authentication has occurred, such as multi-factor authentication.

For more information on the claims in an id_token, see the [v2.0 app model token reference](/documentation/articles/active-directory-v2-tokens).

Once you have completely validated the id_token, you can begin a session with the user and use the claims in the id_token to obtain information about the user in your app.  This information can be used for display, records, authorizations, etc.

## Send a Sign Out Request

The OpenIdConnect `end_session_endpoint` is not currently supported by the v2.0 app model preview. This means your app cannot send a request to the v2.0 endpoint to end a user's session and clear cookies set by the v2.0 endpoint.
To sign a user out, your app can simply end its own session with the user, and leave the user's session with the v2.0 endpoint in-tact.  The next time the user tries to sign in, they will see a "choose account" page, with their actively signed-in accounts listed.
On that page, the user can choose to sign out of any account, ending the session with the v2.0 endpoint.

<!--

When you wish to sign the user out of the  app, it is not sufficient to clear your app's cookies or otherwise end the session with the user.  You must also redirect the user to the v2.0 endpoint for sign out.  If you fail to do so, the user will be able to re-authenticate to your app without entering their credentials again, because they will have a valid single sign-on session with the v2.0 endpoint.

You can simply redirect the user to the `end_session_endpoint` listed in the OpenID Connect metadata document:

```
GET https://login.chinacloudapi.cn/common/oauth2/v2.0/logout?
post_logout_redirect_uri=http%3A%2F%2Flocalhost%2Fmyapp%2F
```

| Parameter | | Description |
| ----------------------- | ------------------------------- | ------------ |
| post_logout_redirect_uri | recommended | The URL which the user should be redirected to after successful logout.  If not included, the user will be shown a generic message by the v2.0 endpoint.  |

-->

## Sign In Summary Diagram
The most basic sign-in flow contains the following steps:

![OpenId Connect Swimlanes](../media/active-directory-v2-flows/convergence_scenarios_webapp.png)

## Get Access Tokens
Many web sites need to not only sign the user in, but also access a web service on behalf of that user using OAuth.  This scenario combines OpenID Connect for user authentication while simultaneously acquiring an authorization_code that can be used to get access_tokens using the OAuth Authorization Code Flow.  To acquire access tokens, you'll need to slightly modify the sign in request from above:


```
// Line breaks for legibility only

GET https://login.chinacloudapi.cn/common/oauth2/v2.0/authorize?
client_id=2d4d11a2-f814-46a7-890a-274a72a7309e		// Your registered Application Id
&response_type=id_token+code
&redirect_uri=http%3A%2F%2Flocalhost%2Fmyapp%2F 	  // Your registered Redirect Uri, url encoded
&response_mode=query							      // 'query', 'form_post', or 'fragment'
&scope=openid%20                                      // Include both 'openid' and scopes your app needs  
offline_access%20										 
https%3A%2F%2Fgraph.chinacloudapi.cn%2Fdirectory.read%20
https%3A%2F%2Fgraph.chinacloudapi.cn%2Fdirectory.write
&state=12345						 				 // Any value, provided by your app
&nonce=678910										 // Any value, provided by your app
```

By including permission scopes in the request and using `response_type=code+id_token`, the v2.0 endpoint will ensure that the user has consented to the permissions indicated in the `scope` query parameter, and return your app an authorization code to exchange for an access token.

A successful response using `response_mode=query` looks like:

```
GET https://localhost/myapp/?
id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik5HVEZ2ZEstZnl0aEV1Q... 	// the id_token, truncated
&code=AwABAAAAvPM1KaPlrEqdFSBzjqfTGBCmLdgfSTLEMPGYuNHSUYBrq... 	// the authorization_code, truncated
&session_state=7B29111D-C220-4263-99AB-6F6E135D75EF			   // a value generated by the v2.0 endpoint
&state=12345												  	// the value provided in the request
&id_token_expires_in=3599

```

| Parameter | Description |
| ----------------------- | ------------------------------- |
| id_token | The id_token that the  app requested. You can use the id_token to verify the user's identity and begin a session with the user.  More details on id_tokens and their contents is included in the [v2.0 app model token reference](/documentation/articles/active-directory-v2-tokens).  |
| code | The authorization_code that the  app requested. The  app can use the authorization code to request an access token for the target resource.  Authorization_codes are very short lived, typically they expire after about 10 minutes. |
| session_state | A unique value that identifies the current user session. This value is a GUID, but should be treated as an opaque value that is passed without examination. |
| state | If a state parameter is included in the request, the same value should appear in the response. The  app should verify that the state values in the request and response are identical. |
| id_token_expires_in | How long the id token is valid (in seconds). |

Error responses may also be sent to the `redirect_uri` so the app can handle them appropriately:

```
GET https://localhost/myapp/?
error=access_denied
&error_description=the+user+canceled+the+authentication
```

| Parameter | Description |
| ----------------------- | ------------------------------- |
| error | An error code string that can be used to classify types of errors that occur, and can be used to react to errors. |
| error_description | A specific error message that can help a developer identify the root cause of an authentication error.  |

Once you've gotten an authorization `code` and an `id_token`, you can sign the user in and get access tokens on their behalf.  To sign the user in, you must validate the `id_token` exactly as described [above](#validating-the-id-token).  To get access tokens, you can follow the steps described in our [OAuth protocol documentation](/documentation/articles/active-directory-v2-protocols-oidc#request-an-access-token).

## Token Acquisition Summary Diagram

For reference, the full OpenID Connect sign-in and token acquisition flow looks something like this:

![OpenId Connect Swimlanes](../media/active-directory-v2-flows/convergence_scenarios_webapp_webapi.png)