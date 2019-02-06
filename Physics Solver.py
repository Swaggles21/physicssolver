# Sebastian Shaffer
# 2/5/2019

def main():
    equationtype = (input('What type of equations are you solving for?\n '))
    if equationtype.lower() in 'linear':
        print('Now solving for Linear equations.')
        global vi, a, t, vf, d, solve, nouse
        solve = (input('Type the variable you would like to solve for: '))
        nouse = (input('Type the variable that will not be used: '))
        vi = float(input('Type a number to represent initial velocity value: '))
        a = float(input('Type a number to represent acceleration value: '))
        t = float(input('Type a number to represent time value in seconds: '))
        vf = float(input('Type a number to represent final velocity value: '))
        d = float(input('Type a number to represent distance value:'))
        if solve == 'a' and nouse == 'd':
            vf = float(input('Final velocity value: '))
            vi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            print((vf - vi) / t)
        # first equation: vf = vi + a*t
        if solve == 'vf' and nouse == 'd':
            a = float(input('Acceleration value: '))
            vi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            print(a * t + vi)
        if solve == 'vi' and nouse == 'd':
            vf = float(input('Final velocity value: '))
            vi = float(input('Initial velocity value: '))
            t = float(input('Seconds: '))
            print(a * t - vf)
        if solve == 't' and nouse == 'd':
            vf = float(input('Final velocity value: '))
            vi = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            var27 = (vf - vi) / a
            print(str(var27) + ' s')
        # second equation: vf^2 = vi^2 + 2*a*d
        if solve == 'vf' and nouse == 't':
            d = float(input('Distance value: '))
            vi = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            var6 = vi ** 2 + 2 * a * d
            print(var6 ** .5)
        if solve == 'vi' and nouse == 't':
            d = float(input('Distance value: '))
            vf = float(input('Final velocity value: '))
            a = float(input('Acceleration value: '))
            var7 = a * 2 * d - vf ** 2
            print(-var7 ** .5)
        if solve == 'a' and nouse == 't':
            d = float(input('Distance value: '))
            vi = float(input('Initial velocity value: '))
            vf = float(input('Final velocity value: '))
            print((vf ** 2 / d) / 2)
        if solve == 'd' and nouse == 't':
            vf = float(input('Final velocity value: '))
            v_i = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            print(((vf ** 2 - v_i ** 2) / a / 2))
        # third equation: d = vi*t + .5*a* t^2
        if solve == 'd' and nouse == 'vf':
            t = float(input('Time in seconds: '))
            v_i = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            print(v_i * t + a * .5 * t ** 2)
        if solve == 'vi' and nouse == 'vf':
            d = float(input('Distance value: '))
            t = float(input('Time in seconds: '))
            a = float(input('Acceleration value: '))
            var11 = .5 * a
            var12 = var11 * t ** 2
            var13 = var12 + t * vi
            print(var13)
        if solve == 'a' and nouse == 'vf':
            d = float(input('Distance value: '))
            vi = float(input('Initial velocity value: '))
            t = float(input('Time in seconds: '))
            var21 = d / t - vi
            var22 = var21 * 2
            print(var22 / t)
        if solve == 't' and nouse == 'vf':
            t = float(input('Time in seconds: '))
            vi = float(input('Initial velocity value: '))
            a = float(input('Acceleration value: '))
            var25 = .5 * a
            var26 = d / var25
            var27 = var26 ** .5
            print(var27)
        # fourth equation: d = (vi + vf)/2 * t
        if solve == 'd' and nouse == 'a':
            t = float(input('Time in seconds: '))
            vi = float(input('Initial velocity value: '))
            vf = float(input('Final velocity value: '))
            var14 = vf + vi
            var15 = var14 / 2
            print(var15 * t)
        if solve == 'vi' and nouse == 'a':
            t = float(input('Fime in seconds: '))
            d = float(input('Distance value: '))
            vf = float(input('Final velocity value: '))
            var23 = 2 * d
            var24 = var23 / t
            print(var24 - vf)
        if solve == 'vf' and nouse == 'a':
            t = float(input('Time in seconds: '))
            vi = float(input('Initial velocity value: '))
            d = float(input('Distance value: '))
            var23 = 2 * d
            var24 = var23 / t
            print(var24 - vi)
        if solve == 't' and nouse == 'a':
            d = float(input('Distance: '))
            vi = float(input('Initial velocity value: '))
            vf = float(input('Final velocity value: '))
            var29 = d / ((vi + vf) / 2)
            print(str(var29) + ' seconds')
        if nouse == 'vi':
            print('An Initial Velocity is always present, if not stated assume it is 0')
            return main()

    elif equationtype.lower() in 'rotational':
        print('Now solving for Rotational equations')
        global ad, avi, avf, aa
        ad = float(input('Type a number to represent Angular Displacement(Theta): '))
        avi = float(input('Type a number to represent initial Angular Velocity(Omega): '))
        avf = float(input('Type a number to represent final Angular Velocity(Omega): '))
        aa = float(input('Type a number to represent Angular Acceleration(Alpha): '))
        t = float(input('Type a number to represent time value: '))
    else:
        print('Please enter either rotational or linear!')
        return main()


main()