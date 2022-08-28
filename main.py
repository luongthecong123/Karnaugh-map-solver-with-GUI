from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from utilities import *


Window.size = (350, 650)

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class MenuScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name = 'menu'))
sm.add_widget(MenuScreen(name = 'biaK1'))
sm.add_widget(MenuScreen(name = 'biaK2bien'))
sm.add_widget(MenuScreen(name = 'biaK3bien'))
sm.add_widget(MenuScreen(name = 'biaK4bien'))
sm.add_widget(MenuScreen(name = 'chuyen'))
sm.add_widget(MenuScreen(name = 'ascii'))
sm.add_widget(MenuScreen(name = 'SOP'))
sm.add_widget(MenuScreen(name = 'ma'))
sm.add_widget(MenuScreen(name = 'about'))

class ChuyenMaScreen(Screen):
    pass
class AboutScreen(Screen):
    pass
class BiaKScreen1(Screen):
    pass
class BiaKScreen2bien(Screen):
    pass
class BiaKScreen3bien(Screen):
    pass
class BiaKScreen4bien(Screen):
    pass

class SOPScreen(Screen):
    pass

class ChuyenCoSoScreen(Screen):
    pass

class DichAsciiScreen(Screen):
    pass
#
# class About(Screen):
#     pass
#
# class Setting(Screen):
#     pass


class Test(MDApp):
    path_to_kv_file = "main.kv"


    to_text = StringProperty() # change base
    to_text_ascii = StringProperty() # ascii
    to_text_SOP = StringProperty()  # SOP to POS
    to_text_POS = StringProperty()  # POS to SOP
    SOPtoPOS_result = StringProperty(defaultvalue='Kết quả: ')
    POStoSOP_result = StringProperty(defaultvalue='Kết quả: ')
    # variable for outputing calculation
    ### change base
    base_from = ""
    base_to = ""
    ### ascii
    base_to_ascii = ""


    # warning:
    to_text_warning_biaK1 = StringProperty()
    #to_text_warning_biaK1 = StringProperty(defaultvalue='hello')

    k_4_0 = StringProperty(defaultvalue='0')
    k_4_1 = StringProperty(defaultvalue='0')
    k_4_2 = StringProperty(defaultvalue='0')
    k_4_3 = StringProperty(defaultvalue='0')
    k_4_4 = StringProperty(defaultvalue='0')
    k_4_5 = StringProperty(defaultvalue='0')
    k_4_6 = StringProperty(defaultvalue='0')
    k_4_7 = StringProperty(defaultvalue='0')
    k_4_8 = StringProperty(defaultvalue='0')
    k_4_9 = StringProperty(defaultvalue='0')
    k_4_10 = StringProperty(defaultvalue='0')
    k_4_11 = StringProperty(defaultvalue='0')
    k_4_12 = StringProperty(defaultvalue='0')
    k_4_13 = StringProperty(defaultvalue='0')
    k_4_14 = StringProperty(defaultvalue='0')
    k_4_15 = StringProperty(defaultvalue='0')
    to_text_SOP_4 = StringProperty(defaultvalue='')


    k_3_0 = StringProperty(defaultvalue='0')
    k_3_1 = StringProperty(defaultvalue='0')
    k_3_2 = StringProperty(defaultvalue='0')
    k_3_3 = StringProperty(defaultvalue='0')
    k_3_4 = StringProperty(defaultvalue='0')
    k_3_5 = StringProperty(defaultvalue='0')
    k_3_6 = StringProperty(defaultvalue='0')
    k_3_7 = StringProperty(defaultvalue='0')
    to_text_SOP_3 = StringProperty(defaultvalue='')


    k_2_0 = StringProperty(defaultvalue='0')
    k_2_1 = StringProperty(defaultvalue='0')
    k_2_2 = StringProperty(defaultvalue='0')
    k_2_3 = StringProperty(defaultvalue='0')
    to_text_SOP_2 = StringProperty(defaultvalue='')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.screen_hot_reload = Builder.load_string(KV)
        self.screen = Builder.load_file("main.kv")


        menu_items_1 = [
            {
                "viewclass": "IconListItem",
                "icon": "arrow-right",
                "text": f"{i}",
                "height": 56,
                "on_release": lambda x=f"{i}": self.set_from(x),
            } for i in ["Binary", "Decimal", "Octal", "Hexadec"]
        ]
        menu_items_2 = [
            {
                "viewclass": "IconListItem",
                "icon": "arrow-right",
                "text": f"{j}",
                "height": 56,
                "on_release": lambda y=f"{j}": self.set_to(y),
            } for j in ["Binary", "Decimal", "Octal", "Hexadec"]
        ]

        menu_items_ascii = [
            {
                "viewclass": "IconListItem",
                "icon": "arrow-right",
                "text": f"{k}",
                "height": 56,
                "on_release": lambda z=f"{k}": self.set_ascii(z),
            } for k in ["Binary", "Decimal", "Octal", "Hexadec"]
        ]

        menu_items_ma_1 = [
            {
                "viewclass": "IconListItem",
                "icon": "arrow-right",
                "text": f"{k}",
                "height": 56,
                "on_release": lambda z=f"{k}": self.set_ma_from(z),
            } for k in ["BCD", "Excess-3", "2421", "Gray"]
        ]

        menu_items_ma_2 = [
            {
                "viewclass": "IconListItem",
                "icon": "arrow-right",
                "text": f"{k}",
                "height": 56,
                "on_release": lambda z=f"{k}": self.set_ma_to(z),
            } for k in ["BCD", "Excess-3", "2421", "Gray"]
        ]
        self.menu_1 = MDDropdownMenu(
            caller=self.screen.get_screen('chuyen').ids.drop_item_1,
            #caller=self.screen.ids.drop_item_1,
            items=menu_items_1,
            position="bottom",
            width_mult=4,
        )
        self.menu_2 = MDDropdownMenu(
            caller=self.screen.get_screen('chuyen').ids.drop_item_2,
            items=menu_items_2,
            position="center",
            width_mult=4,
        )

        self.menu_ascii = MDDropdownMenu(
            caller=self.screen.get_screen('ascii').ids.drop_item_ascii,
            items=menu_items_ascii,
            position="center",
            width_mult=4,
        )

        self.menu_ma_1 = MDDropdownMenu(
            caller=self.screen.get_screen('ma').ids.drop_item_ma_1,
            items=menu_items_ma_1,
            position="bottom",
            width_mult=4,
        )

        self.menu_ma_2 = MDDropdownMenu(
            caller=self.screen.get_screen('ma').ids.drop_item_ma_2,
            items=menu_items_ma_2,
            position="center",
            width_mult=4,
        )

        self.menu_1.bind()
        self.menu_2.bind()
        self.menu_ascii.bind()
        self.menu_ma_1.bind()
        self.menu_ma_2.bind()

###################### methods for convert menu #################
    def set_from(self, text_item):
        self.screen.get_screen('chuyen').ids.drop_item_1.set_item(text_item)
        self.menu_1.dismiss()

        # interfere
        # select base takes string and return integer
        Test.base_from = select_base(text_item) # user's choice

    def set_to(self, text_item):
        self.screen.get_screen('chuyen').ids.drop_item_2.set_item(text_item)
        self.menu_2.dismiss()

        # interfere
        # select base takes string and return integer
        Test.base_to = select_base(text_item) # user's choice

    def convert_GUI(self):

        if (Test.base_to == "") or (Test.base_from == ""):
            return 0

        self.to_text = convert(self.screen.get_screen('chuyen').ids.from_text_id.text,
                                Test.base_from, Test.base_to)
###################### methods for ascii menu #################
    def set_ascii(self, text_item):
        self.screen.get_screen('ascii').ids.drop_item_ascii.set_item(text_item)
        self.menu_ascii.dismiss()

        Test.base_to_ascii = select_base(text_item)

    def ascii_decode_GUI(self):
        if (Test.base_to_ascii == "") :
            return 0
        ascii_text = self.screen.get_screen('ascii').ids.from_text_id_ascii.text
        ascii_bin = ascii_decode(ascii_text)

        self.to_text_ascii = convert(ascii_bin, 2, Test.base_to_ascii)
###################### methods for K menu #################
    def set_k(self, text_item):
        self.screen.get_screen('biaK1').ids.drop_item_k.set_item(text_item)
        self.menu_k.dismiss()

        # interfere
        #print(text_item)
        # select base takes string and return integer
        Test.var_num = select_var_num(text_item) # user's choice
        print(Test.var_num)
######################## methods for ma #####################
    def set_ma_from(self, text_item):
        pass
    def set_ma_to(self, text_item):
        pass
########################### 4 BIEN ##########################
    def switch_4_0(self):
        if self.k_4_0 == '0': self.k_4_0 = '1'
        elif self.k_4_0 == '1': self.k_4_0 = 'X'
        elif self.k_4_0 == 'X': self.k_4_0 = '0'
    def switch_4_1 (self):
     if self.k_4_1 == '0': self.k_4_1 = '1'
     elif self.k_4_1 == '1': self.k_4_1 = 'X'
     elif self.k_4_1 == 'X': self.k_4_1 = '0'
    def switch_4_2 (self):
     if self.k_4_2 == '0': self.k_4_2 = '1'
     elif self.k_4_2 == '1': self.k_4_2 = 'X'
     elif self.k_4_2 == 'X': self.k_4_2 = '0'
    def switch_4_3 (self):
     if self.k_4_3 == '0': self.k_4_3 = '1'
     elif self.k_4_3 == '1': self.k_4_3 = 'X'
     elif self.k_4_3 == 'X': self.k_4_3 = '0'
    def switch_4_4 (self):
     if self.k_4_4 == '0': self.k_4_4 = '1'
     elif self.k_4_4 == '1': self.k_4_4 = 'X'
     elif self.k_4_4 == 'X': self.k_4_4 = '0'
    def switch_4_5 (self):
     if self.k_4_5 == '0': self.k_4_5 = '1'
     elif self.k_4_5 == '1': self.k_4_5 = 'X'
     elif self.k_4_5 == 'X': self.k_4_5 = '0'
    def switch_4_6 (self):
     if self.k_4_6 == '0': self.k_4_6 = '1'
     elif self.k_4_6 == '1': self.k_4_6 = 'X'
     elif self.k_4_6 == 'X': self.k_4_6 = '0'
    def switch_4_7 (self):
     if self.k_4_7 == '0': self.k_4_7 = '1'
     elif self.k_4_7 == '1': self.k_4_7 = 'X'
     elif self.k_4_7 == 'X': self.k_4_7 = '0'
    def switch_4_8 (self):
     if self.k_4_8 == '0': self.k_4_8 = '1'
     elif self.k_4_8 == '1': self.k_4_8 = 'X'
     elif self.k_4_8 == 'X': self.k_4_8 = '0'
    def switch_4_9 (self):
     if self.k_4_9 == '0': self.k_4_9 = '1'
     elif self.k_4_9 == '1': self.k_4_9 = 'X'
     elif self.k_4_9 == 'X': self.k_4_9 = '0'
    def switch_4_10 (self):
     if self.k_4_10 == '0': self.k_4_10 = '1'
     elif self.k_4_10 == '1': self.k_4_10 = 'X'
     elif self.k_4_10 == 'X': self.k_4_10 = '0'
    def switch_4_11 (self):
     if self.k_4_11 == '0': self.k_4_11 = '1'
     elif self.k_4_11 == '1': self.k_4_11 = 'X'
     elif self.k_4_11 == 'X': self.k_4_11 = '0'
    def switch_4_12 (self):
     if self.k_4_12 == '0': self.k_4_12 = '1'
     elif self.k_4_12 == '1': self.k_4_12 = 'X'
     elif self.k_4_12 == 'X': self.k_4_12 = '0'
    def switch_4_13 (self):
     if self.k_4_13 == '0': self.k_4_13 = '1'
     elif self.k_4_13 == '1': self.k_4_13 = 'X'
     elif self.k_4_13 == 'X': self.k_4_13 = '0'
    def switch_4_14 (self):
     if self.k_4_14 == '0': self.k_4_14 = '1'
     elif self.k_4_14 == '1': self.k_4_14 = 'X'
     elif self.k_4_14 == 'X': self.k_4_14 = '0'
    def switch_4_15 (self):
     if self.k_4_15 == '0': self.k_4_15 = '1'
     elif self.k_4_15 == '1': self.k_4_15 = 'X'
     elif self.k_4_15 == 'X': self.k_4_15 = '0'

    def rut_gon_K_4(self):
        str_4 = ''
        str_4_d = ''
        if self.screen.get_screen('biaK4bien').ids.k_4_0.text == '1': str_4 = str_4 + '0,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_0.text == 'X': str_4_d = str_4_d + '0,'
        if self.screen.get_screen('biaK4bien').ids.k_4_1.text == '1': str_4 = str_4 + '1,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_1.text == 'X': str_4_d = str_4_d + '1,'
        if self.screen.get_screen('biaK4bien').ids.k_4_2.text == '1': str_4 = str_4 + '2,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_2.text == 'X': str_4_d = str_4_d + '2,'
        if self.screen.get_screen('biaK4bien').ids.k_4_3.text == '1': str_4 = str_4 + '3,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_3.text == 'X': str_4_d = str_4_d + '3,'
        if self.screen.get_screen('biaK4bien').ids.k_4_4.text == '1': str_4 = str_4 + '4,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_4.text == 'X': str_4_d = str_4_d + '4,'
        if self.screen.get_screen('biaK4bien').ids.k_4_5.text == '1': str_4 = str_4 + '5,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_5.text == 'X': str_4_d = str_4_d + '5,'
        if self.screen.get_screen('biaK4bien').ids.k_4_6.text == '1': str_4 = str_4 + '6,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_6.text == 'X': str_4_d = str_4_d + '6,'
        if self.screen.get_screen('biaK4bien').ids.k_4_7.text == '1': str_4 = str_4 + '7,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_7.text == 'X': str_4_d = str_4_d + '7,'
        if self.screen.get_screen('biaK4bien').ids.k_4_8.text == '1': str_4 = str_4 + '8,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_8.text == 'X': str_4_d = str_4_d + '8,'
        if self.screen.get_screen('biaK4bien').ids.k_4_9.text == '1': str_4 = str_4 + '9,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_9.text == 'X': str_4_d = str_4_d + '9,'
        if self.screen.get_screen('biaK4bien').ids.k_4_10.text == '1': str_4 = str_4 + '10,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_10.text == 'X': str_4_d = str_4_d + '10,'
        if self.screen.get_screen('biaK4bien').ids.k_4_11.text == '1': str_4 = str_4 + '11,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_11.text == 'X': str_4_d = str_4_d + '11,'
        if self.screen.get_screen('biaK4bien').ids.k_4_12.text == '1': str_4 = str_4 + '12,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_12.text == 'X': str_4_d = str_4_d + '12,'
        if self.screen.get_screen('biaK4bien').ids.k_4_13.text == '1': str_4 = str_4 + '13,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_13.text == 'X': str_4_d = str_4_d + '13,'
        if self.screen.get_screen('biaK4bien').ids.k_4_14.text == '1': str_4 = str_4 + '14,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_14.text == 'X': str_4_d = str_4_d + '14,'
        if self.screen.get_screen('biaK4bien').ids.k_4_15.text == '1': str_4 = str_4 + '15,'
        elif self.screen.get_screen('biaK4bien').ids.k_4_15.text == 'X': str_4_d = str_4_d + '15,'

        if str_4 == '':
            print(" Cảnh báo: K map phải có bit 1 !")
            self.to_text_SOP_4 = "0"
            return 0
        else: str_4 = str_4[0:-1]

        if len(str(str_4)) == 37:
            self.to_text_SOP_4 = "1"
            return 0

        if str_4_d != '':
            str_4_d = str_4_d[0:-1]

        print("str_4: ", str_4)
        print("str_4_d: ", str_4_d)
        print("str_4: len", len(str(str_4)))

        if str_4_d == '':
            str_k = '(' + str_4 + ')' + 'd-'
        else:
            str_k = '(' + str_4 + ')' + 'd(' + str_4_d + ')'
        SOP_4 = minFunc('4', str_k)
        self.to_text_SOP_4 = SOP_4

        print("Kết quả: ", SOP_4)


    def reset_4(self):
        self.screen.get_screen('biaK4bien').ids.k_4_0.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_1.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_2.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_3.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_4.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_5.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_6.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_7.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_8.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_9.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_10.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_11.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_12.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_13.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_14.text = '0'
        self.screen.get_screen('biaK4bien').ids.k_4_15.text = '0'
        self.to_text_SOP_4 = ''

########################### 3 BIEN ##########################
    def switch_3_0 (self):
     if self.k_3_0 == '0': self.k_3_0 = '1'
     elif self.k_3_0 == '1': self.k_3_0 = 'X'
     elif self.k_3_0 == 'X': self.k_3_0 = '0'
    def switch_3_1 (self):
     if self.k_3_1 == '0': self.k_3_1 = '1'
     elif self.k_3_1 == '1': self.k_3_1 = 'X'
     elif self.k_3_1 == 'X': self.k_3_1 = '0'
    def switch_3_2 (self):
     if self.k_3_2 == '0': self.k_3_2 = '1'
     elif self.k_3_2 == '1': self.k_3_2 = 'X'
     elif self.k_3_2 == 'X': self.k_3_2 = '0'
    def switch_3_3 (self):
     if self.k_3_3 == '0': self.k_3_3 = '1'
     elif self.k_3_3 == '1': self.k_3_3 = 'X'
     elif self.k_3_3 == 'X': self.k_3_3 = '0'
    def switch_3_4 (self):
     if self.k_3_4 == '0': self.k_3_4 = '1'
     elif self.k_3_4 == '1': self.k_3_4 = 'X'
     elif self.k_3_4 == 'X': self.k_3_4 = '0'
    def switch_3_5 (self):
     if self.k_3_5 == '0': self.k_3_5 = '1'
     elif self.k_3_5 == '1': self.k_3_5 = 'X'
     elif self.k_3_5 == 'X': self.k_3_5 = '0'
    def switch_3_6 (self):
     if self.k_3_6 == '0': self.k_3_6 = '1'
     elif self.k_3_6 == '1': self.k_3_6 = 'X'
     elif self.k_3_6 == 'X': self.k_3_6 = '0'
    def switch_3_7 (self):
     if self.k_3_7 == '0': self.k_3_7 = '1'
     elif self.k_3_7 == '1': self.k_3_7 = 'X'
     elif self.k_3_7 == 'X': self.k_3_7 = '0'


    def rut_gon_K_3(self):
        str_3 = ''
        str_3_d = ''
        if self.screen.get_screen('biaK3bien').ids.k_3_0.text == '1': str_3 = str_3 + '0,'
        elif self.screen.get_screen('biaK3bien').ids.k_3_0.text == 'X': str_3_d = str_3_d + '0,'
        if self.screen.get_screen('biaK3bien').ids.k_3_1.text == '1': str_3 = str_3 + '1,'
        elif self.screen.get_screen('biaK3bien').ids.k_3_1.text == 'X': str_3_d = str_3_d + '1,'
        if self.screen.get_screen('biaK3bien').ids.k_3_2.text == '1': str_3 = str_3 + '2,'
        elif self.screen.get_screen('biaK3bien').ids.k_3_2.text == 'X': str_3_d = str_3_d + '2,'
        if self.screen.get_screen('biaK3bien').ids.k_3_3.text == '1': str_3 = str_3 + '3,'
        elif self.screen.get_screen('biaK3bien').ids.k_3_3.text == 'X': str_3_d = str_3_d + '3,'
        if self.screen.get_screen('biaK3bien').ids.k_3_4.text == '1': str_3 = str_3 + '4,'
        elif self.screen.get_screen('biaK3bien').ids.k_3_4.text == 'X': str_3_d = str_3_d + '4,'
        if self.screen.get_screen('biaK3bien').ids.k_3_5.text == '1': str_3 = str_3 + '5,'
        elif self.screen.get_screen('biaK3bien').ids.k_3_5.text == 'X': str_3_d = str_3_d + '5,'
        if self.screen.get_screen('biaK3bien').ids.k_3_6.text == '1': str_3 = str_3 + '6,'
        elif self.screen.get_screen('biaK3bien').ids.k_3_6.text == 'X': str_3_d = str_3_d + '6,'
        if self.screen.get_screen('biaK3bien').ids.k_3_7.text == '1': str_3 = str_3 + '7,'
        elif self.screen.get_screen('biaK3bien').ids.k_3_7.text == 'X': str_3_d = str_3_d + '7,'

        if str_3 == '':
            print(" Cảnh báo: K map phải có bit 1 !")
            self.to_text_SOP_3 = "0"
            return 0
        else: str_3 = str_3[0:-1]

        if len(str(str_3)) == 15:
            self.to_text_SOP_3 = "1"
            return 0

        if str_3_d != '':
            str_3_d = str_3_d[0:-1]

        print("str_3: ", str_3)
        print("str_3_d: ", str_3_d)
        print("str_3: len", len(str_3))

        if str_3_d == '':
            str_k = '(' + str_3 + ')' + 'd-'
        else:
            str_k = '(' + str_3 + ')' + 'd(' + str_3_d + ')'
        SOP_3 = minFunc('3', str_k)
        self.to_text_SOP_3 = SOP_3

        print("Kết quả: ", SOP_3)

    def reset_3(self):
        self.screen.get_screen('biaK3bien').ids.k_3_0.text = '0'
        self.screen.get_screen('biaK3bien').ids.k_3_1.text = '0'
        self.screen.get_screen('biaK3bien').ids.k_3_2.text = '0'
        self.screen.get_screen('biaK3bien').ids.k_3_3.text = '0'
        self.screen.get_screen('biaK3bien').ids.k_3_4.text = '0'
        self.screen.get_screen('biaK3bien').ids.k_3_5.text = '0'
        self.screen.get_screen('biaK3bien').ids.k_3_6.text = '0'
        self.screen.get_screen('biaK3bien').ids.k_3_7.text = '0'
        self.to_text_SOP_3 = ''

########################### 2 BIEN ##########################
    def switch_2_0 (self):
     if self.k_2_0 == '0': self.k_2_0 = '1'
     elif self.k_2_0 == '1': self.k_2_0 = 'X'
     elif self.k_2_0 == 'X': self.k_2_0 = '0'
    def switch_2_1 (self):
     if self.k_2_1 == '0': self.k_2_1 = '1'
     elif self.k_2_1 == '1': self.k_2_1 = 'X'
     elif self.k_2_1 == 'X': self.k_2_1 = '0'
    def switch_2_2 (self):
     if self.k_2_2 == '0': self.k_2_2 = '1'
     elif self.k_2_2 == '1': self.k_2_2 = 'X'
     elif self.k_2_2 == 'X': self.k_2_2 = '0'
    def switch_2_3 (self):
     if self.k_2_3 == '0': self.k_2_3 = '1'
     elif self.k_2_3 == '1': self.k_2_3 = 'X'
     elif self.k_2_3 == 'X': self.k_2_3 = '0'

    def rut_gon_K_2(self):
        str_2 = ''
        str_2_d = ''
        if self.screen.get_screen('biaK2bien').ids.k_2_0.text == '1': str_2 = str_2 + '0,'
        elif self.screen.get_screen('biaK2bien').ids.k_2_0.text == 'X': str_2_d = str_2_d + '0,'
        if self.screen.get_screen('biaK2bien').ids.k_2_1.text == '1': str_2 = str_2 + '1,'
        elif self.screen.get_screen('biaK2bien').ids.k_2_1.text == 'X': str_2_d = str_2_d + '1,'
        if self.screen.get_screen('biaK2bien').ids.k_2_2.text == '1': str_2 = str_2 + '2,'
        elif self.screen.get_screen('biaK2bien').ids.k_2_2.text == 'X': str_2_d = str_2_d + '2,'
        if self.screen.get_screen('biaK2bien').ids.k_2_3.text == '1': str_2 = str_2 + '3,'
        elif self.screen.get_screen('biaK2bien').ids.k_2_3.text == 'X': str_2_d = str_2_d + '3,'

        if str_2 == '':
            print(" Cảnh báo: K map phải có bit 1 !")
            self.to_text_SOP_2 = "0"
            return 0
        else: str_2 = str_2[0:-1]

        if len(str(str_2)) == 7:
            self.to_text_SOP_2 = "1"
            return 0

        if str_2_d != '':
            str_2_d = str_2_d[0:-1]

        print("str_2: ", str_2)
        print("str_2_d: ", str_2_d)
        print("str_2: len", len(str_2))

        if str_2_d == '':
            str_k = '(' + str_2 + ')' + 'd-'
        else:
            str_k = '(' + str_2 + ')' + 'd(' + str_2_d + ')'
        SOP_2 = minFunc('2', str_k)
        self.to_text_SOP_2 = SOP_2

        print("Kết quả: ", SOP_2)

    def reset_2(self):
        self.screen.get_screen('biaK2bien').ids.k_2_0.text = '0'
        self.screen.get_screen('biaK2bien').ids.k_2_1.text = '0'
        self.screen.get_screen('biaK2bien').ids.k_2_2.text = '0'
        self.screen.get_screen('biaK2bien').ids.k_2_3.text = '0'
        self.to_text_SOP_2 = ''

    ########################## POS #################################
    def SOPtoPOS(self):
        SOP_text = self.screen.get_screen('SOP').ids.from_text_SOP.text
        #print(SOP_text)
        self.SOPtoPOS_result = get_POS(SOP_text)

    def POStoSOP(self):
        POS_text = self.screen.get_screen('SOP').ids.from_text_POS.text
        #print(POS_text)
        self.POStoSOP_result = get_SOP(POS_text)


    def build(self):
        return self.screen

Test().run()
