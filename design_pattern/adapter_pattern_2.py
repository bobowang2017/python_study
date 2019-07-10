class ACpnStaff(object):
    name = ""
    id = ""
    phone = ""

    def __init__(self, id):
        self.id = id

    def getName(self):
        print("A protocol getName method ..id:%s" % self.id)
        return self.name

    def setName(self, name):
        print("A protocol setName method ..id:%s" % self.id)
        self.name = name

    def getPhone(self):
        print("A protocol getPhone method ..id:%s" % self.id)
        return self.phone

    def setPhone(self, phone):
        print("A protocol setPhone method ..id:%s" % self.id)
        self.phone = phone


class BCpnStaff(object):
    name = ""
    id = ""
    telephone = ""

    def __init__(self, id):
        self.id = id

    def getName(self):
        print("B protocol getName method ..id:%s" % self.id)
        return self.name

    def setName(self, name):
        print("B protocol setName method ..id:%s" % self.id)
        self.name = name

    def getPhone(self):
        print("B protocol getPhone method ..id:%s" % self.id)
        return self.telephone

    def setPhone(self, telephone):
        print("B protocol setPhone method ..id:%s" % self.id)
        self.telephone = telephone


class CpnStaffAdapter:
    b_cpn = ""

    def __init__(self, id):
        self.b_cpn = BCpnStaff(id)

    def getName(self):
        return self.b_cpn.getName()

    def getPhone(self):
        return self.b_cpn.getPhone()

    def setName(self, name):
        self.b_cpn.setName(name)

    def setPhone(self, phone):
        self.b_cpn.setPhone(phone)


if __name__ == "__main__":
    acpn_staff = ACpnStaff("123")
    acpn_staff.setPhone("wuzi")
    acpn_staff.setName("wuzi1")
    bcpn_staff = CpnStaffAdapter("456")
    bcpn_staff.setName("wuzib")
    bcpn_staff.setPhone("phoneb")
