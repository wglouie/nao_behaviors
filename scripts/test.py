#!/usr/bin/env python

from naoqi import ALProxy
import webbrowser
import time
import pyautogui #https://pyautogui.readthedocs.io/en/latest/cheatsheet.html#keyboard-functions
#from pynput.keyboard import Key, Controller #https://pypi.org/project/pynput/
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    time.sleep(1)
    webbrowser.open("https://bright626816.github.io/")

    #Delay to wait for page to load
    time.sleep(5)

    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[-0.0413762, [3, -0.0133333, 0], [3, 0.52, 0]], [-0.325165, [3, -0.52, 0.0719783], [3, 0.333333, -0.0461399]], [-0.395731, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.167164, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[-0.745566, [3, -0.0133333, 0], [3, 0.52, 0]], [-1.17969, [3, -0.52, 0.0239326], [3, 0.333333, -0.0153414]], [-1.19503, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.790051, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[0.0296, [3, -0.0133333, 0], [3, 0.52, 0]], [0.304, [3, -0.52, 0], [3, 0.333333, 0]], [0.2904, [3, -0.333333, 0.0136], [3, 0.333333, -0.0136]], [0.0748, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[1.48334, [3, -0.0133333, 0], [3, 0.52, 0]], [1.52169, [3, -0.52, 0], [3, 0.333333, 0]], [1.50021, [3, -0.333333, 0.0214763], [3, 0.333333, -0.0214763]], [1.32687, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[0.202446, [3, -0.0133333, 0], [3, 0.52, 0]], [0.0797259, [3, -0.52, 0], [3, 0.333333, 0]], [0.154892, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0153821, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[-0.817664, [3, -0.0133333, 0], [3, 0.52, 0]], [0.0981341, [3, -0.52, 0], [3, 0.333333, 0]], [0.0843279, [3, -0.333333, 0.0138063], [3, 0.333333, -0.0138063]], [-0.753235, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[0.030722, [3, -0.0133333, 0], [3, 0.52, 0]], [1.51563, [3, -0.52, 0], [3, 0.333333, 0]], [1.44967, [3, -0.333333, 0.0659613], [3, 0.333333, -0.0659613]], [0.165714, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[0.837522, [3, -0.0133333, 0], [3, 0.52, 0]], [2.08926, [3, -0.52, 0], [3, 0.333333, 0]], [0.67952, [3, -0.333333, 0], [3, 0.333333, 0]], [0.993989, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[0.0384001, [3, -0.0133333, 0], [3, 0.52, 0]], [0.852, [3, -0.52, 0], [3, 0.333333, 0]], [0.314, [3, -0.333333, 0.126667], [3, 0.333333, -0.126667]], [0.092, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[1.55245, [3, -0.0133333, 0], [3, 0.52, 0]], [0.546147, [3, -0.52, 0], [3, 0.333333, 0]], [0.737896, [3, -0.333333, -0.134736], [3, 0.333333, 0.134736]], [1.35456, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[-0.159578, [3, -0.0133333, 0], [3, 0.52, 0]], [-0.285367, [3, -0.52, 0], [3, 0.333333, 0]], [0.329768, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0245859, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0, 1.56, 2.56, 3.56])
    keys.append([[0.673385, [3, -0.0133333, 0], [3, 0.52, 0]], [-0.135034, [3, -0.52, 0], [3, 0.333333, 0]], [-0.0844118, [3, -0.333333, -0.0506222], [3, 0.333333, 0.0506222]], [0.435615, [3, -0.333333, 0], [3, 0, 0]]])

    try:
      # uncomment the following line and modify the IP for real robot
      #motion = ALProxy("ALMotion", "nao.local", 9559)
      # uncomment for choreographe simulation      
      motion = ALProxy("ALMotion", "127.0.0.1", 44525)
      motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
      print err

    time.sleep(1.56)

    # Press and release space
    pyautogui.keyDown("right")
    pyautogui.keyUp("right")

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
