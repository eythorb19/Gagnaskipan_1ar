class pbor_class:

    def __init__(self,inst_var):
        self.inst_var = inst_var   #tilviksbreyta (instance)


    def reassign(self):
        print("inst_var before reassign: " + str(self.inst_var))
        self.inst_var = [0,1]
        print("inst_var after reassign: " + str(self.inst_var))

    def change(self):
        print("inst_var before change: " + str(self.inst_var))
        self.inst_var.append(1)
        print("inst_var after change: " + str(self.inst_var))