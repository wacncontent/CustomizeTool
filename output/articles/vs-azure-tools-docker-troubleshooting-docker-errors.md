<properties
   pageTitle="Troubleshooting Docker Client Errors on Windows Using Visual Studio | Microsoft Azure"
   description="Troubleshoot problems you encounter when using Visual Studio to create and deploy web apps to Docker on Windows by using Visual Studio."
   services="visual-studio-online"
   documentationCenter="na"
   authors="kempb"
   manager="douge"
   editor="tglee" />
<tags
   ms.service="multiple"
   ms.devlang="dotnet"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="multiple"
   ms.date="08/20/2015"
   ms.author="kempb" />

# Troubleshooting Docker Errors

After you configure all of the settings for your app's Docker container, you should make sure the settings and paths are correct. Visual Studio provides a Validate button in the Publish dialog to help you do this.

This topic helps you diagnose and either fix or work around the most common problems you'll encounter when hosting a Visual Studio app in Docker. More issues will be added to this topic as they're encountered.

## You get a failed message when you attempt to validate the connection to your Docker host in the Publish Web dialog box

Here are some possible solutions to this issue.

- In the **Connection** tab of the **Publish** dialog, make sure the **Server Url** is correct and that the trailing `:<port_number>` on the **Server URL** is the port that the Docker daemon is listening to.

- In the **Connection** tab of the **Publish** dialog, expand the **Docker Advanced Options** section and ensure that the correct **Auth** Options are being specified.
  - If the Docker daemon on the server is configured to use TLS security then the Windows Docker command line interface (docker.exe) will look for the client key (key.pem) and certificate (cert.pem) by default under the `<%userprofile%>\.docker` folder. If these items aren't present they will need to be generated by using OpenSSL. For more information on configuring Docker for TLS, see [Protecting the Docker daemon Socket with HTTPS](https://docs.docker.com/articles/https/).

	One way to ensure that Docker is properly authenticating from the Windows client to the Linux server is by copying the contents of the Preview text box into a new command window and changing `<command>` to "info" as in the following:

    ```
    // This example assumes the Docker daemon is configured to use the default port
    // of 2376 to listen for connections.docker.

    --tls -H tcp://contoso.cloudapp.net:2376 info
    ```

    As an alternative to copying the client cert and key files to the .docker folder, you can change the **Auth** Options by adding the following parameters:

    ```
    --tls --tlscert=C:\mycert\cert.pem --tlskey=C:\mycert\key.pem
    ```
- Ensure the Docker daemon on the Docker host machine is version 1.6 or later.

## Timeout error when using your own certificates without client certificate in the Docker folder

If you choose to use your own certificates when creating the Docker host in Visual Studio (that is, you clear the **Auto-generate Docker certificates** check box in the **Create virtual machine on Microsoft Azure** dialog box), you'll need to copy the client certificate and key files (cert.pem and key.pem) to the Docker folder (`<%userprofile%>\.docker`). Otherwise, when you publish your project, you'll get a timeout error in one hour and the publish operation will fail.

## PowerShell 3.0 required to publish to Docker containers

If your operating system is Windows 7 or Windows Server 2008, you'll need to install PowerShell 3.0 before you can publish to Docker containers. PowerShell 3.0 is included in [Windows Management Framework 3.0](https://www.microsoft.com/en-us/download/details.aspx?id=34595). You'll need to reboot your system after installing it.

As an alternative workaround, you can upgrade to Windows 8.1 or Windows 10, which already has PowerShell 3.0.

## PowerShell window does not automatically close

After creating a VM, sometimes the PowerShell window does not close automatically. Closing this window also closes Visual Studio. Because the window does not affect any Visual Studio or Docker tools features, please leave it open until you finish your work.

## FAQ

Q: How do I create a new Docker-enabled Linux machine in Azure using the Visual Studio tools?

A: See [Hosting Web Apps in Docker](vs-azure-tools-docker-hosting-web-apps-in-docker.md) for information on how to do this.

Q:  What Visual Studio project templates are supported for publishing to a Linux Docker container?

A:  Visual Studio currently supports the C# Console Application (Package) and C# ASP.NET 5 Preview web templates, including:

- Empty

- Web API

- Web Application

Q:  How do I publish my ASP.NET 5 web or console project to Docker using MSBUILD from the command line?

A:  Use the following MSBuild command:

    `msbuild <projectname.xproj> /p:deployOnBuild=true;publishProfile=<profilename>`

Q:  How do I publish my ASP.NET 5 web or console project to Docker using PowerShell from the command line?

A:  Use the following PowerShell command:

```
.\contoso-Docker-publish.ps1 -packOutput $env:USERPROFILE\AppData\Local\Temp\PublishTemp -pubxmlFile .\contoso-Docker.pubxml
```

Q:  I have my own Linux server with Docker installed, how do I specify this in the **Web Publish** dialog?

A:  See the section **Provide a Custom Docker Host** in the topic, [Hosting Web Apps in Docker](vs-azure-tools-docker-hosting-web-apps-in-docker.md).

Q:  I'm using my own Linux server with Docker installed. How do I generate keys and certificates in order to configure authentication using TLS?

A:  One way is to use OpenSSL on the server to generate the required certificates and keys for the CA, server, and client. You can then use third party software to establish an SSH/SFTP connection, and then copy the certificates to the local Windows development machine. By default, the Docker (CLI) will attempt to use certificates located in the `<userprofile>\.docker` folder.

Another option is to download OpenSSL for Windows and generate the required certificates and keys, and then upload the CA, server certificates, and keys to the Linux machine. For more information on establishing a secure connection to Docker, see [Protecting the Docker daemon Socket with HTTPS](https://docs.docker.com/articles/https/).