# Manufacturing and Assembly

## Table of contents
 - [Overview](#OVER)
 - [Part Manufacturing](#MANUFACTURING)
 - [Assembly Brief](#ASSEMBLY)

## 1 Overview and Toolset <a id="OVER"></a>
Here you can find manufacturing and assembly details for a single Pulse Oximeter device. Download all the files for 3D printing from the build_files folder

<img src="https://user-images.githubusercontent.com/14543226/31544259-31640a3e-b01a-11e7-83d4-df441b65fae5.jpg" alt="step5a" width= "300" >

### 1.1 General
- Manufacturing time:
  - 3D printing - 6h
  - soldering (1 unit by hand, depends on the skills) - 2h
- Assembly time: 10min

### 1.2 Tool List
- Screw set:
  - 4 pcs. M2.5x5mm screws DIN7985 or similar
  - 4 pcs. M3x14mm screws DIN965 or similar
  - 2 pcs. M3x10mm screws DIN965 or similar
  - 4 pcs. M3x6mm screws DIN7985 or similar

- Drill set:
  - 2mm drill
  - 2.5mm drill
  - 3mm drill
  - chamfer drill

- Philips screwdriver
- Battery Hand Drill

### 1.4 Parts list

All parts can be found in build_files folder.

Finger clamp:
- finger_clamp (.STL)(.STEP)
- top_cover (.STL)(.STEP)
- bottom_cover (.STL)(.STEP)

Case:
- case_bottom (.STL)(.STEP)
- case_top (.STL)(.STEP)
- spacer (.STL)(.STEP)


## 2 Part Manufacturing <a id="MANUFACTURING"></a>

- 3D print all the parts

  Print settings:
- Cut/peel away the brim on the parts with a knife or similar
- Hole widening: widen the holes and drill chamfers as marked on the scheme

## 3 Assembly <a id="ASSEMBLY"></a>

### 3.1 Assembly Overview
 - manufacture all parts
 - first assemble each section separately, then join them together, as shown in the assembly brief

### 3.2 Assembly Details

**Finger clip**

Collect the necessary parts: 3D printed parts, soldered finger clip kit, screws.

<img src="https://user-images.githubusercontent.com/14543226/31542108-0d6c389e-b011-11e7-92fb-b08a54904dde.jpg" alt="step2b" width= "300" >

| DESCRIPTION | STEP 1 | STEP 2 |
|------|-------|-------|
|Insert two M3x5mm screws into the top cover holes, place the PCB with the sensor on top of the top cover so the screws go through the holes on the PCB and the cables are all hidden behind the PCB|<img src="https://user-images.githubusercontent.com/14543226/31542507-96ce28d0-b012-11e7-9367-3b5a16d2859a.jpg" alt="step3a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31542513-a2e1c28a-b012-11e7-8933-6371fc235b17.jpg" alt="step3b" width= "300" >|
|Repeat the process for the bottom cover and PCB with the LEDs |<img src="https://user-images.githubusercontent.com/14543226/31542531-b52a79f0-b012-11e7-9142-d321f8b742c9.jpg" alt="step4a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31542549-c2f20170-b012-11e7-8382-a5f48253a1d6.jpg" alt="step4b" width= "300" >|
|Place the top cover on the side of the finger clip with the UTP cable cutout and fasten the two screws. If you can still move the cable once the screws are fastened, dismount the top cover and use hot glue to fill the space in the cable slot.|<img src="https://user-images.githubusercontent.com/14543226/31542581-da321aaa-b012-11e7-9d7d-116cc3bf753b.jpg" alt="step5a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31542592-e652f64c-b012-11e7-901b-1c3354297761.jpg" alt="step5b" width= "300" >|
|Place the bottom cover on the opposite side of the finger clamp and fasten the two screws|<img src="https://user-images.githubusercontent.com/14543226/31542603-f3700b4e-b012-11e7-8eed-d3aef9ecface.jpg" alt="step6a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31542604-f39215ea-b012-11e7-96c3-1156393d6faa.jpg" alt="step6b" width= "300" >|

**Case**

Collect the necessary parts: 3D printed parts, PCB, screws.

<img src="https://user-images.githubusercontent.com/14543226/31542750-a121953c-b013-11e7-875e-9eee97162037.jpg" alt="step2b" width= "300" >



| DESCRIPTION | STEP 1 | STEP 2 |
|------|-------|-------|
|Place the screen into the slot on the case_bottom|<img src="https://user-images.githubusercontent.com/14543226/31542788-bafc7b34-b013-11e7-8c2b-92a9eea73629.jpg" alt="step2a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31542789-bb1caa30-b013-11e7-9aa2-478f8c68a60e.jpg" alt="step2b" width= "300" >|
|Place the main PCB on the spacer so the connector cables go through the cutout and fix them together with four M2.5x5mm screws|<img src="https://user-images.githubusercontent.com/14543226/31542860-0763d7f6-b014-11e7-848b-eff8216ec9d0.jpg" alt="step3a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31542861-077efad6-b014-11e7-9f8d-d025ec5507aa.jpg" alt="step3b" width= "300" >|
|Place the spacer on the case_bottom over the screen and place the connector in its position before fastening in the two M3x10mm screws on the spacer|<img src="https://user-images.githubusercontent.com/14543226/31542884-24f8725e-b014-11e7-8652-e27553908158.jpg" alt="step4a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31542886-25139d18-b014-11e7-9ed2-aa79fca817b0.jpg" alt="step4b" width= "300" >|
|Connect the screen with the main PCB by pulling the slider on the connector out to insert the cable and pushing it back in to lock it in|<img src="https://user-images.githubusercontent.com/14543226/31543691-a4291bca-b017-11e7-85dd-a34bf48ccb22.jpg" alt="step5a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31543690-a40cd6fe-b017-11e7-9ba5-237249d15075.jpg" alt="step5b" width= "300" >|
|Plug in the battery and place the battery next to the spacer.|<img src="https://user-images.githubusercontent.com/14543226/31543723-c80e2f62-b017-11e7-8382-5470ac710bdb.jpg" alt="step6a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31543721-c7ee550c-b017-11e7-834f-0d1b5eeca64b.jpg" alt="step6b" width= "300" >|
|Put on the case_top and screw in the four M3x14mm screws|<img src="https://user-images.githubusercontent.com/14543226/31543752-ec4fd6c8-b017-11e7-9997-2d589a24a2d6.jpg" alt="step7a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31543745-e1c9fcce-b017-11e7-8064-850378420036.jpg" alt="step7b" width= "300" >|

Plug it the UTP cable from the finger clamp into the connector on the case to finish the assembly.

<img src="https://user-images.githubusercontent.com/14543226/31543752-ec4fd6c8-b017-11e7-9997-2d589a24a2d6.jpg" alt="step8a" width= "300" >|<img src="https://user-images.githubusercontent.com/14543226/31544308-74150b94-b01a-11e7-8d57-62f8fc99e2ef.jpg" alt="step8b" width= "300" >

Turn on the pulse oximeter and check whether you can see any light through the narrow slip between the finger LED cover and the finger clip. If yes, tighten the screws until you can no longer see light passing through. Be aware not to tighten the screws too much - you can destroy threads in the plastic. Moreover, UTP wires must be handled with care since they are very prone to tearing.

**TESTING**

<img src="https://user-images.githubusercontent.com/14543226/31544384-d7fff5f6-b01a-11e7-8ba9-64b61a96d534.jpg" alt="step8b" width= "300" >

CONGRATULATIONS! You've assembled your GliaX pulse oximeter. To test if your device works as it should see test_procedure folder.
