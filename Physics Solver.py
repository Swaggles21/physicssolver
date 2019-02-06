# Sebastian Shaffer
# 2/5/2019

def main():
    equationtype = (input('What type of equations are you solving for?\n '))
    if equationtype.lower() in 'linear':
        print('Now solving for Linear equations.')
        vi = float(input('Type a number to represent initial velocity value: '))
        a = float(input('Type a number to represent acceleration value: '))
        t = float(input('Type a number to represent time value: '))
        vf = float(input('Type a number to represent final velocity value: '))
        d = float(input('Type a number to represent distance value:'))

    elif equationtype.lower() in 'rotational':
        print('Now solving for Rotational equations')
        AD = float(input('Type a number to represent Angular Displacement(Theta): '))
        AVI = float(input('Type a number to represent initial Angular Velocity(Omega): '))
        AVF = float(input('Type a number to represent final Angular Velocity(Omega): '))
        AA = float(input('Type a number to represent Angular Acceleration(Alpha): '))
        t = float(input('Type a number to represent time value: '))
    else:
        print('Please enter either rotational or linear!')
        return main()


main()