<!--author=SharS last changed: 12/01/15-->

#### To enter Maintenance mode

1. In the serial console menu, choose option 1, **Log in with full access**.

2. Type the password. The default password is **Password1**.

3. At the command prompt, type

     `Enter-HcsMaintenanceMode`

4. You will see a warning message telling you that Maintenance mode will disrupt all I/O requests and sever the connection to the Azure Management Portal, and you will be prompted for confirmation. Type **Y** to enter Maintenance mode.

    Both controllers will restart. When the restart is complete, another message will appear indicating that the device is in Maintenance mode.
