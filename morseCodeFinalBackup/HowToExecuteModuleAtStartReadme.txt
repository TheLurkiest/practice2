

Created by: Brent Fanning and Xavier Doyle


Getting our Python Code to Execute Automatically each time the Raspberry Pi is turned on:
------------------------------------------------------------------------------------------

This was a relatively simple process—first we created an empty text file and then we copied the following into it (since we would need to
repeat this whole procedure for every single pi we were working with) to create a shell script:

------------------------------------------------------------------------------------------

POINTLESS="stuff"
echo $POINTLESS
HOPEFULTEST="harmless2.py"
echo $HOPEFULTEST
#sudo python $HOPEFULTEST
sudo python3 /home/pi/pyAtStart/$HOPEFULTEST

------------------------------------------------------------------------------------------


This shell script first does some pointless stuff just for show and then runs our python code harmless2.py saved within the variable
“$HOPEFULTEST.”
Then we changed our permissions by entering chmod 777 bmanScript4 to allow us to use it.

------------------------------------------------------------------------------------------

Finally we then simply went to our ~ using cd ~ if not already there and then began altering .bashrc by entering sudo nano .bashrc into the
terminal. Then we simply scrolled down to the very bottom and added the following line to the very end ./bmanScript4
...this of course would set us up so that our python code would automatically run at the start every time we reset our pi. In order to shut this
off if we no longer want it happening anymore, we can simply comment out that last line we added making it #./bmanScript4
...until we decide we need it again at which point we can, of course, simply uncomment it.

------------------------------------------------------------------------------------------


...obviously in order to make this work you'll need to plug in whatever you decide to name this module-- and whatever location you decide to place it-- for us, we just called the module "harmless2.py"-- and we put it in the following location: /home/pi/pyAtStart/
...however, if you're not using a raspberry pi, you'll probably want to name the directories something different-- just make sure you stay consistent in your shell script.
