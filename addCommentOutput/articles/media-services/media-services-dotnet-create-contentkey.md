<properties 
	pageTitle="Create ContentKeys with .NET" 
	description="Learn how to create content keys that provide secure access to Assets." 
	services="media-services" 
	documentationCenter="" 
	authors="Juliako" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="12/05/2015"
	wacn.date=""/>


#Create ContentKeys with .NET

> [AZURE.SELECTOR]
- [REST](/documentation/articles/media-services-rest-create-contentkey)
- [.NET](/documentation/articles/media-services-dotnet-create-contentkey)

Media Services enables you to create and deliver encrypted assets. A **ContentKey** provides secure access to your **Asset**s. 

When you create a new asset (for example, before you [upload files](/documentation/articles/media-services-dotnet-upload-files)), you can specify the following encryption options: **StorageEncrypted**, **CommonEncryptionProtected**, or **EnvelopeEncryptionProtected**. 

When you deliver assets to your clients, you can [configure for assets to be dynamically encrypted](/documentation/articles/media-services-dotnet-configure-asset-delivery-policy) with one of the following two encryptions: **DynamicEnvelopeEncryption** or **DynamicCommonEncryption**.

Encrypted assets have to be associated with **ContentKey**s. This article describes how to create a content key.

>[AZURE.NOTE] When creating a new **StorageEncrypted** asset using the Media Services .NET SDK , the **ContentKey** is automatically created and linked with the asset.

##ContentKeyType

One of the values that you must set when create a content key is the content key type. Choose from one of the following values. 

    public enum ContentKeyType
    {
        /// <summary>
        /// Specifies a content key for common encryption.
        /// </summary>
        /// <remarks>This is the default value.</remarks>
        CommonEncryption = 0,

        /// <summary>
        /// Specifies a content key for storage encryption.
        /// </summary>
        StorageEncryption = 1,

        /// <summary>
        /// Specifies a content key for configuration encryption.
        /// </summary>
        ConfigurationEncryption = 2,

        /// <summary>
        /// Specifies a content key for Envelope encryption.  Only used internally.
        /// </summary>
        EnvelopeEncryption = 4
    }

##<a id="envelope_contentkey"></a>Create envelope type ContentKey

The following code snippet creates a content key of the envelope encryption type. It then associates the key with the specified asset.

    static public IContentKey CreateEnvelopeTypeContentKey(IAsset asset)
    {
        // Create envelope encryption content key
        Guid keyId = Guid.NewGuid();
        byte[] contentKey = GetRandomBuffer(16);

        IContentKey key = _context.ContentKeys.Create(
                                keyId,
                                contentKey,
                                "ContentKey",
                                ContentKeyType.EnvelopeEncryption);

        asset.ContentKeys.Add(key);

        return key;
    }

    static private byte[] GetRandomBuffer(int size)
    {
        byte[] randomBytes = new byte[size];
        using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
        {
            rng.GetBytes(randomBytes);
        }

        return randomBytes;
    }

call

	IContentKey key = CreateEnvelopeTypeContentKey(encryptedsset);



##<a id="common_contentkey"></a>Create common type ContentKey    

The following code snippet creates a content key of the common encryption type. It then associates the key with the specified asset.

    static public IContentKey CreateCommonTypeContentKey(IAsset asset)
    {
        // Create common encryption content key
        Guid keyId = Guid.NewGuid();
        byte[] contentKey = GetRandomBuffer(16);

        IContentKey key = _context.ContentKeys.Create(
                                keyId,
                                contentKey,
                                "ContentKey",
                                ContentKeyType.CommonEncryption);

        // Associate the key with the asset.
        asset.ContentKeys.Add(key);

        return key;
    }

    static private byte[] GetRandomBuffer(int length)
    {
        var returnValue = new byte[length];

        using (var rng =
            new System.Security.Cryptography.RNGCryptoServiceProvider())
        {
            rng.GetBytes(returnValue);
        }

        return returnValue;
    }
call

	IContentKey key = CreateCommonTypeContentKey(encryptedsset); 


<!-- deleted by customization
##Media Services learning paths

[AZURE.INCLUDE [media-services-learning-paths-include](../includes/media-services-learning-paths-include.md)]

##Provide feedback

[AZURE.INCLUDE [media-services-user-voice-include](../includes/media-services-user-voice-include.md)]
-->
