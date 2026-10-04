if ratio > 1.38:
            st.session_state.face_shape = "کشیده (Oblong / Long Face)"
            st.session_state.frames = [
                {
                    "id": "aviator", 
                    "name": "Tom Ford - Aviator Gold", 
                    "type": "خلبانی فلزی لوکس کلاسیک", 
                    "brand": "Tom Ford", 
                    # استفاده از تصاویر با فرمت مناسب و بدون پس‌زمینه کادری
                    "url": "https://www.pngarts.com/files/3/Aviator-Sunglasses-PNG-High-Quality-Image.png"
                },
                {
                    "id": "wayfarer", 
                    "name": "Ray-Ban - Wayfarer Classic", 
                    "type": "مستطیلی کائوچویی مشکی استاندارد", 
                    "brand": "Ray-Ban", 
                    "url": "https://www.pngarts.com/files/1/Sunglasses-PNG-Background-Image.png"
                }
            ]
        elif 1.18 <= ratio <= 1.38:
            st.session_state.face_shape = "بیضی متعادل (Oval - استاندارد طلایی)"
            st.session_state.frames = [
                {
                    "id": "wayfarer", 
                    "name": "Ray-Ban - Wayfarer Classic", 
                    "type": "ویفرر استاندارد شیک", 
                    "brand": "Ray-Ban", 
                    "url": "https://www.pngarts.com/files/1/Sunglasses-PNG-Background-Image.png"
                },
                {
                    "id": "cateye", 
                    "name": "Tom Ford - Elegant CatEye", 
                    "type": "چشم‌‌گربه‌ای مدرن و جذاب", 
                    "brand": "Tom Ford", 
                    "url": "https://www.pngarts.com/files/3/Sunglasses-PNG-Transparent-Image.png"
                }
            ]
        else:
            st.session_state.face_shape = "گرد یا مربعی (Round / Square)"
            st.session_state.frames = [
                {
                    "id": "round", 
                    "name": "Ray-Ban - Retro Round Metal", 
                    "type": "گرد فلزی مینیمال مهندسی‌شده", 
                    "brand": "Ray-Ban", 
                    "url": "https://www.pngarts.com/files/3/Round-Sunglasses-PNG-Image-Background.png"
                },
                {
                    "id": "slim", 
                    "name": "Tom Ford - Slim Rectangular", 
                    "type": "فریم زاویه‌‌دار باریک", 
                    "brand": "Tom Ford", 
                    "url": "https://www.pngarts.com/files/3/Sunglasses-PNG-Image.png"
                }
            ]