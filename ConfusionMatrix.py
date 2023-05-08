class ConfusionMatrix():
    def __init__(self, outputs, y_true):
        self.y_pred= np.array(outputs.argmax(axis= 1))
        y_true= np.array(y_true)
        self.TP = 0
        self.TN = 0
        self.FP = 0
        self.FN = 0
        # print y_pred to confirm how it looks like!
        positive= 0
        for j in range(len(self.y_pred)):
            self.TP += (self.y_pred[j]==positive) & (y_true[j]== positive)
            self.TN += (self.y_pred[j]!=positive) & (y_true[j]!= positive)
            self.FP += (self.y_pred[j]==positive) & (y_true[j]!= positive)
            self.FN += (self.y_pred[j]!=positive) & (y_true[j]== positive)
    def ruler(self):
        print(self.TN, self.FP, self.FN, self.TP)
    def recall(self):
        return(round(self.TP / ((self.TP + self.FN)+0.0000001), 4))
    def precision(self):
        return(round(self.TP / ((self.TP + self.FP)+0.0000001), 4))
    def accuracy(self):
        return(round((self.TP+ self.TN) / ((self.TP + self.TN + self.FP + self.FN)+0.0000001), 4))
    def f1_score(self): 
        return(round(2*self.TP / ((2*self.TP + self.FP + self.FN)+0.0000001), 4))
