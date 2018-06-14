# network_switch_data_streamer
Framework that decides the sending data

This Framework gets the responsibility of deciding the type of sendind data from the application.

It requires that an object that can have access to the types of flow. This object has to have methods that return the data that is going to be sent and a method that return this as functions references in a list in order of load (0 is the lightest)

videos from http://www.viratdata.org/
