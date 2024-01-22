 
            
#_______________________-----------------------------_________________________________________________
            
            
        
                
            
            
                
        
        
            
                
        
#: include SignUpPage.kv


AuthMainLayout:
<mimi@Widget>:

    
<AuthMainLayout>:
    #orientation:"vertical"
    canvas.before:
        Color:
            rgba:0,0,1,1
        Rectangle:
            pos:self.pos
            size:self.size
    BoxLayout:
        size_hint:.9,None
        #size:
        height:600
        
        orientation:"vertical"
        pos_hint:{"center_x":.5,"center_y":.5}
            
        #size_hint_y:None
        #height:self.minimum_height
        spacing:"30dp"
        canvas.before:
            Color:
                rgba:1,1,1,1
            Rectangle:
                pos:self.pos
                size:self.size
                source:"C:/code/serious_work/ios app for mr david/ElitePage_kivy/resource/Rectangle 877.png"
        Label:
            size_hint:1,.01
        BoxLayout:
            id:u_ib
            pos_hint:{"center_x":.5,}
            #size_hint:1,.12
            size_hint:1,None
            #padding:"20dp"
            size:70,150
            #pos_hint:{"center_x":.5,"center_y":.5}
            canvas.before:
                Color:
                    rgba:0,1,1,.5
                Rectangle:
                    pos:self.pos
                    size:self.size
            Image:
                pos_hint:{"center_x":.5,"center_y":.5}
                #center:u_ib.center
                source:"C:/code/serious_work/ios app for mr david/ElitePage_kivy/resource/rhs 2.png"
                
            #Button:
                #text:"why"
                #size_hint:None,None
                #size:50,90
                #pos_hint:{"center_x":.5}
        ElevatedTextInput:
            pos_hint:{"center_x":.5}
            size_hint:.9,None
            size:300,50
        BoxLayout:
            #padding:["10dp","1dp","10dp","10dp"]
            orientation:"vertical"
            pos_hint:{"center_x":.5}
            size_hint:.9,None
            size:300,110
            spacing:"7dp"
            ElevatedTextInput:
                pos_hint:{"center_x":.5}
                size_hint:1,None
                size:300,50
            Button:
                text:"Forgot Password?"
                #background_color:0,0,0,0
                color:.1,.1,.1,1
                size_hint:1,None
                height:"12dp"
                font_size:"12dp"
                
                text_size:self.size
        SmartButton:
            size_hint:None,None
            size:137,37
            pos_hint:{'right':.9}
            text: "Login"
            background_color:0,0,0,0
            #bold:True
            font_size:"25dp"
            canvas.before:
                Color:
                    rgba:0.00, 0.50, 0.00,1
                RoundedRectangle:
                    pos:self.pos
                    size:self.size
                    
                    radius:[17]
                

        Label:
            size_hint:1,.1
        
