def remplieY(Y, i):
    return (float(Y[i])) #Valeur que l'on doit trouver


def remplieX(X, i):
    temp = []
    for j in range(len(X)):
        temp.append(float(X[j][i]))  # Données rassemblées pour ensuite être transmisent à X_train
    return temp


def remplieTabY(Y, i):
    Y[i][0]=float(Y[i][0])
    Y[i][1]=float(Y[i][1])
    return Y[i]