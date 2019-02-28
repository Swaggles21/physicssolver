# Sebastian Shaffer
# 2/5/2019

import math

def main():
    equationtype = (input('What type of equations are you solving for(Linear, Rotational, Torque)?\n '))
    if equationtype.lower() in 'linear':
        print('Now solving for Linear equations.')
        print('Possible variables are vi / a / t / vf / d.')
        solve = (input('Type the variable you would like to solve for: '))
        nouse = (input('Type the variable that will not be used: '))
        if solve.lower() in 'a' and nouse == 'd':
            vf = float(input('Final velocity value: '))
            vi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            print('Answer:', (vf - vi) / t)
        if solve == 'vf' and nouse == 'd':
            a = float(input('Acceleration value: '))
            vi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            print('Answer: ', a * t + vi)
        if solve == 'vi' and nouse == 'd':
            vf = float(input('Final velocity value: '))
            vi = float(input('Initial velocity value: '))
            t = float(input('Seconds: '))
            print('Answer:', a * t - vf)
        if solve == 't' and nouse == 'd':
            vf = float(input('Final velocity value: '))
            vi = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            var27 = (vf - vi) / a
            print('Answer:', str(var27) + ' s')
        if solve == 'vf' and nouse == 't':
            d = float(input('Distance value: '))
            vi = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            var6 = vi ** 2 + 2 * a * d
            print('Answer:', var6 ** .5)
        if solve == 'vi' and nouse == 't':
            d = float(input('Distance value: '))
            vf = float(input('Final velocity value: '))
            a = float(input('Acceleration value: '))
            var7 = a * 2 * d - vf ** 2
            print('Answer:', -var7 ** .5)
        if solve == 'a' and nouse == 't':
            d = float(input('Distance value: '))
            vi = float(input('Initial velocity value: '))
            vf = float(input('Final velocity value: '))
            print('Answer:', (vf ** 2 / d) / 2)
        if solve == 'd' and nouse == 't':
            vf = float(input('Final velocity value: '))
            v_i = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            print('Answer:', ((vf ** 2 - v_i ** 2) / a / 2))
        if solve == 'd' and nouse == 'vf':
            t = float(input('Time in seconds: '))
            v_i = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            print('Answer:', v_i * t + a * .5 * t ** 2)
        if solve == 'vi' and nouse == 'vf':
            d = float(input('Distance value: '))
            t = float(input('Time in seconds: '))
            a = float(input('Acceleration value: '))
            var11 = .5 * a
            var12 = var11 * t ** 2
            var13 = var12 + t * vi
            print('Answer:', var13)
        if solve == 'a' and nouse == 'vf':
            d = float(input('Distance value: '))
            vi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            var21 = d / t - vi
            var22 = var21 * 2
            print('Answer:', var22 / t)
        if solve == 't' and nouse == 'vf':
            vi = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            d = float(input('Distance value: '))
            var25 = .5 * a
            var26 = d / var25
            var27 = var26 ** .5
            print('Answer:', var27)
        if solve == 'd' and nouse == 'a':
            t = float(input('Time in seconds: '))
            vi = float(input('Initial velocity value: '))
            vf = float(input('Final velocity value: '))
            var14 = vf + vi
            var15 = var14 / 2
            print('Answer:', var15 * t)
        if solve == 'vi' and nouse == 'a':
            t = float(input('Time in seconds: '))
            d = float(input('Distance value: '))
            vf = float(input('Final velocity value: '))
            var23 = 2 * d
            var24 = var23 / t
            print('Answer:', var24 - vf)
        if solve == 'vf' and nouse == 'a':
            t = float(input('Time in seconds: '))
            vi = float(input('Initial velocity value: '))
            d = float(input('Distance value: '))
            var23 = 2 * d
            var24 = var23 / t
            print('Answer:', var24 - vi)
        if solve == 't' and nouse == 'a':
            d = float(input('Distance: '))
            vi = float(input('Initial velocity value: '))
            vf = float(input('Final velocity value: '))
            var29 = d / ((vi + vf) / 2)
            print('Answer:', str(var29) + ' seconds')
        if nouse == 'vi':
            print('An Initial Velocity is always present, if not stated assume it is 0')
            return main()

    elif equationtype.lower() in 'rotational':
        print('Now solving for Rotational equations')
        print('Note:\n'
              'ad represents Angular Displacement\n'
              'avi represents Initial Angular Velocity\n'
              'avf represents Final Angular Velocity\n'
              'aa represents Angular Acceleration\n'
              't represents time\n')
        solve = (input('Type the variable you would like to solve for: '))
        nouse = (input('Type the variable that will not be used: '))

        if solve.lower() in 'avi' and nouse == 'ad':
            avf = float(input('Final velocity value: '))
            avi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            print('Answer:', (avf - avi) / t)
        if solve == 'avf' and nouse == 'ad':
            aa = float(input('Acceleration value: '))
            avi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            print('Answer: ', aa * t + avi)
        if solve == 'avi' and nouse == 'ad':
            avf = float(input('Final velocity value: '))
            avi = float(input('Initial velocity value: '))
            t = float(input('Seconds: '))
            print('Answer:', aa * t - avf)
        if solve == 't' and nouse == 'ad':
            avf = float(input('Final velocity value: '))
            avi = float(input('Initial velocity value: '))
            aa = float(input('Acceleration value: '))
            var27 = (avf - avi) / aa
            print('Answer:', str(var27) + ' s')
        if solve == 'avf' and nouse == 't':
            ad = float(input('Distance value: '))
            avi = float(input('Initial velocity value: '))
            aa = float(input('Acceleration value: '))
            var6 = avi ** 2 + 2 * aa * ad
            print('Answer:', var6 ** .5)
        if solve == 'avi' and nouse == 't':
            ad = float(input('Distance value: '))
            avf = float(input('Final velocity value: '))
            aa = float(input('Acceleration value: '))
            var7 = aa * 2 * ad - avf ** 2
            print('Answer:', -var7 ** .5)
        if solve == 'aa' and nouse == 't':
            ad = float(input('Distance value: '))
            avi = float(input('Initial velocity value: '))
            avf = float(input('Final velocity value: '))
            print('Answer:', (avf ** 2 / ad) / 2)
        if solve == 'ad' and nouse == 't':
            avf = float(input('Final velocity value: '))
            avi = float(input('Initial velocity value: '))
            aa = float(input('Acceleration value: '))
            print('Answer:', ((avf ** 2 - avi ** 2) / aa / 2))
        if solve == 'ad' and nouse == 'avf':
            t = float(input('Time in seconds: '))
            avi = float(input('Initial velocity value: '))
            aa = float(input('Acceleration value: '))
            print('Answer:', avi * t + aa * .5 * t ** 2)
        if solve == 'avi' and nouse == 'avf':
            ad = float(input('Distance value: '))
            t = float(input('Time in seconds: '))
            aa = float(input('Acceleration value: '))
            var11 = .5 * aa
            var12 = var11 * t ** 2
            var13 = var12 + t * avi
            print('Answer:', var13)
        if solve == 'aa' and nouse == 'avf':
            ad = float(input('Distance value: '))
            avi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            var21 = ad / t - avi
            var22 = var21 * 2
            print('Answer:', var22 / t)
        if solve == 't' and nouse == 'avf':
            avi = float(input('Initial velocity value: '))
            aa = float(input('Acceleration value: '))
            ad = float(input('Distance value: '))
            var25 = .5 * aa
            var26 = ad / var25
            print('Answer:', var26)
        if solve == 'ad' and nouse == 'aa':
            t = float(input('Time in seconds: '))
            avi = float(input('Initial velocity value: '))
            avf = float(input('Final velocity value: '))
            var14 = avf + avi
            var15 = var14 / 2
            print('Answer:', var15 * t)
        if solve == 'avi' and nouse == 'aa':
            t = float(input('Time in seconds: '))
            ad = float(input('Distance value: '))
            avf = float(input('Final velocity value: '))
            var23 = 2 * ad
            var24 = var23 / t
            print('Answer:', var24 - avf)
        if solve == 'avf' and nouse == 'aa':
            t = float(input('Time in seconds: '))
            avi = float(input('Initial velocity value: '))
            ad = float(input('Distance value: '))
            var23 = 2 * ad
            var24 = var23 / t
            print('Answer:', var24 - avi)
        if solve == 't' and nouse == 'aa':
            ad = float(input('Distance: '))
            avi = float(input('Initial velocity value: '))
            avf = float(input('Final velocity value: '))
            var29 = ad / ((avi + avf) / 2)
            print('Answer:', str(var29) + ' seconds')
        if nouse == 'avi':
            print('An Initial Velocity is always present, if not stated assume it is 0')
            return main()

    elif equationtype.lower() in 'torque':
        print('Now solving for Torque')
        print('Note:\n'
              'a represents Angle\n'
              'r represents Radius/Distance\n'
              'f represents Force\n'
              't represents Torque\n')
        solve = (input('What variable are you solving for?\n'))
        if solve.lower() in 'r':
            a = float(input('Angel in Degrees: '))
            f = float(input('Force: '))
            t = float(input('Torque: '))
            print('Answer:', (t / f * (math.sin(math.radians(a)))), 'Meters')
        if solve.lower() in 'f':
            a = float(input('Angel in Degrees: '))
            r = float(input('Radius/Distance: '))
            t = float(input('Torque: '))
            print('Answer:', (t / r * (math.sin(math.radians(a)))), 'Newtons')
        if solve.lower() in 't':
            a = float(input('Angel in Degrees: '))
            f = float(input('Force: '))
            r = float(input('Radius/Distance: '))
            print('Answer:', (r * f * (math.sin(math.radians(a)))), 'Newton Meters')
            return main()
            
    else:
        print('Please enter either rotational, linear or torque!')
        return main()


main()
