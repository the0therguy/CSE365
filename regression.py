import random


def regression(w, x1, x2, x3):
    y = w[0] + (w[1] * x1) + (w[2] * x2) + (w[3] * x3)

    return y


def slope(y_pred, y):
    slope = []
    for i in range(len(y_pred)):
        s = (y_pred[i] - y[i])
        slope.append(s)

    return sum(slope)


def other_slope(y_pred, y, x):
    slope = []
    for i in range(len(y_pred)):
        s = (y_pred[i] - y[i]) * x[i]
        # print((y_pred[i], "-", y[i]), "*", x[i])
        slope.append(s)

    return sum(slope)


if __name__ == '__main__':

    with open('dataRegression.txt', 'r') as file:
        a = file.read()
    x1, x2, x3, y = [], [], [], []
    for i in a.split('\n'):
        if len(i) > 1:
            y.append(float(i.split(',')[3]))
            x1.append(float(i.split(',')[0]))
            x2.append(float(i.split(',')[1]))
            x3.append(float(i.split(',')[2]))
    w = []
    for i in range(0, 4):
        a = random.random()
        w.append(a)
    print("random W:", w)
    with open('w.txt', 'w') as file:
        file.write(str(w))
        file.write("\n")
    y_pred = []
    for i in range(0, len(x1)):
        y_cap = regression(w, x1[i], x2[i], x3[i])
        y_pred.append(y_cap)
    # print("y prediction:", y_pred)

    learning_rate = float(input("Enter learning rate: "))
    w0_new = w[0] - (learning_rate * (slope(y_pred, y)))
    w1_new = w[1] - (learning_rate * other_slope(y_pred, y, x1))
    w2_new = w[2] - (learning_rate * other_slope(y_pred, y, x2))
    w3_new = w[3] - (learning_rate * other_slope(y_pred, y, x3))
    w.clear()
    w = [w0_new, w1_new, w2_new, w3_new]
    with open('w.txt', 'a') as file:
        file.write("new w:")
        file.write(str(w))

    print("new W:", w)

    x1_val = float(input("Enter the value: "))
    x2_val = float(input("Enter the value: "))
    x3_val = float(input("Enter the value: "))
    print("Input Predicted Value: ", regression(w, x1_val, x2_val, x3_val))
