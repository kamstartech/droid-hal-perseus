# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device perseus
%define vendor xiaomi
%define droid_target_aarch64 1
%define lunch_device hadk_perseus-bp1a
%define device_variant -userdebug

%define vendor_pretty Xiaomi
%define device_pretty Mix 3

%define installable_zip 1

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"
