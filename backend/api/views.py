from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import CartItemSerializer
# Create your views here.
class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
@csrf_exempt
@api_view(["POST"])
def add_cart_items(request):
    errors = []
    print(request.data)
    # Iterate over each item in the request data
    for x in request.data['cartItems']:
        print(x)
        # Prepare data for the serializer
        data = {
            # "customer_id":x[""],
            "product_id": x['id'],
            "product_name": x['description'],
            "quantity": x['quantity'],
            "subtotal": x['total'],
            "contact":x["contact"],
            "address": x['address'],
          

        }
        
        # Initialize the serializer with the data
        serializer = CartItemSerializer(data=data)
        
        # Check if the data is valid
        if serializer.is_valid():
            # Save the valid data
            serializer.save()
        else:
            # Collect errors if the data is invalid
             errors.append(serializer.errors)
    
    # If there are any errors, return them
    if errors:
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Return success response if all items are added successfully
    return Response({"message": "All items added to cart successfully."}, status=status.HTTP_201_CREATED)
def data(request):
    # Updated ProductsData with corrected image links
    ProductsData = [
        {
            'id': 10,
            'type': "clock",
            'price': 66000,
            'description': "Vintage Style Resin and Brass Clocks",
            'detaildescription': "Inspired by classic designs, these vintage-style clocks combine resin with brass elements to create a timeless piece. The brass detailing adds a touch of elegance, while the resin components provide durability and a modern twist.",
            'rating': 4.0,
            'review': 205,
            'img': "https://i.ibb.co/WsLgXz9/w4.jpg"
        },
        {
            'id': 4,
            'type': "clock",
            'price': 58000,
            'description': "Minimalist Resin Wall Clocks with Metal Inlays",
            'detaildescription': "For those who appreciate clean lines and modern design, these minimalist wall clocks are a perfect choice. The resin face is complemented by subtle metal inlays.",
            'rating': 4.5,
            'review': 170,
            'img': "https://i.ibb.co/xgBFRS3/w2.webp"
        },
        {
            'id': 12,
            'type': "sculpture",
            'price': 86000,
            'description': "Elegant Resin Busts for Home Decor",
            'detaildescription': "These resin busts are masterfully crafted to capture the essence of classical sculpture. Perfect for adding a touch of sophistication to your home.",
            'rating': 3.5,
            'review': 195,
            'img': "https://i.ibb.co/xq3vtGG/s4.webp"
        },
        {
            'id': 5,
            'type': "decoration",
            'price': 29000,
            'description': "Handcrafted Resin and Wood Decorative Bowls",
            'detaildescription': "These bowls create a beautiful contrast between the natural grain of the wood and the smooth resin. Excellent centerpieces in any room.",
            'rating': 4.5,
            'review': 140,
            'img': "https://i.ibb.co/BPFNs5r/p2.jpg"
        },
{ 
    "id": 6, 
    "type": "sculpture", 
    "price": 92000, 
    "description": "Abstract Resin Sculptures for Modern Interiors", 
    "detaildescription": "Perfect for contemporary art lovers, these abstract resin sculptures feature fluid, dynamic forms that bring a sense of movement and energy to any space. The vibrant colors and unique shapes make them a focal point in any room.",
    "rating": 5, 
    "review": 220, 
    "img": "https://i.ibb.co/tCNdB7C/s2.webp"
  },
 
  { 
    "id": 9, 
    "type": "sculpture", 
    "price": 78000, 
    "description": "Custom Resin Animal Sculptures", 
    "detaildescription": "Each of these animal sculptures is custom-made, capturing the beauty and spirit of wildlife. The detailed craftsmanship and lifelike appearance make them a great addition to any nature lover's collection.",
    "rating": 4.0, 
    "review": 175, 
    "img": "https://i.ibb.co/0VnzjbX/s3.webp" 
  },
  { 
    "id": 15, 
    "type": "sculpture", 
    "price": 88000, 
    "description": "Life-Like Resin Human Figurines", 
    "detaildescription": "These human figurines are designed to be as lifelike as possible, with intricate details and realistic poses. They are perfect for anyone who appreciates the beauty of the human form in art.",
    "rating": 4.0, 
    "review": 210, 
    "img": "https://i.ibb.co/4J39CsW/s5.webp" 
  },
  { 
    "id": 11, 
    "type": "decoration", 
    "price": 45000, 
    "description": "Luxurious Resin and Crystal Centerpieces", 
    "detaildescription": "These centerpieces are a blend of resin and crystal, creating a luxurious look that is perfect for formal dining rooms or living spaces. The sparkling crystal elements catch the light beautifully, making these pieces a stunning focal point.",
    "rating": 5, 
    "review": 230, 
    "img": "https://i.ibb.co/nkCGW4X/s10.jpg"
  },
  { 
    "id": 13, 
    "type": "clock", 
    "price": 60000, 
    "description": "Modern Resin and LED Wall Clocks", 
    "detaildescription": "These wall clocks feature a modern design with built-in LED lighting that adds a contemporary touch to any space. The combination of resin and light creates a unique visual effect, making these clocks both functional and decorative.",
    "rating": 4.0, 
    "review": 180, 
    "img": "https://i.ibb.co/FbdkxHH/w7.jpg" 
  },
  { 
    "id": 8, 
    "type": "decoration", 
    "price": 39000, 
    "description": "Colorful Resin Decorative Plates", 
    "detaildescription": "These decorative plates are made from resin and feature vibrant colors and intricate patterns. They are perfect for adding a pop of color to any room and can be displayed on walls or used as functional serving pieces.",
    "rating": 4.5, 
    "review": 160, 
    "img": "https://i.ibb.co/YTPvMYq/p3.webp"
  },
  { 
    "id": 3, 
    "type": "sculpture", 
    "price": 84000, 
    "description": "Exquisite Resin Sculptures for Art Enthusiasts", 
    "detaildescription": "These sculptures are crafted with attention to detail, making them perfect for art enthusiasts who appreciate fine craftsmanship. The resin material allows for intricate designs that are both durable and visually striking.",
    "rating": 4.5, 
    "review": 180, 
    "img": "https://i.ibb.co/LC6WSxn/s1.webp" 
  },
  { 
    "id": 14, 
    "type": "decoration", 
    "price": 32000, 
    "description": "Hand-Painted Resin Wall Art Pieces", 
    "detaildescription": "Each of these wall art pieces is hand-painted, making them unique and full of character. The resin material provides a durable base for the vibrant colors and intricate designs, making these pieces a perfect addition to any room.",
    "rating": 5, 
    "review": 150, 
    "img": "https://i.ibb.co/xq3vtGG/s13.webp" 
  },
  { 
    "id": 2, 
    "type": "decoration", 
    "price": 34000, 
    "description": "Elegant Resin Decorations to Elevate Your Space", 
    "detaildescription": "These elegant resin decorations are designed to elevate any space with their stylish and sophisticated look. Perfect for adding a touch of luxury to your home, they are versatile enough to complement any decor style.",
    "rating": 4.0, 
    "review": 150, 
    "img": "https://i.ibb.co/8xm2gHN/p1.webp" 
  },
  { 
    "id": 16, 
    "type": "decoration", 
    "price": 40000, 
    "description": "Elegant Resin Decorative Plate with Intricate Patterns", 
    "detaildescription": "This decorative plate features a beautiful resin finish with intricate patterns, making it an elegant addition to any room. Perfect for display or as a functional serving piece.",
    "rating": 4.5, 
    "review": 155, 
    "img": "https://i.ibb.co/X4JHStB/p3.jpg" 
  },
  { 
    "id": 17, 
    "type": "decoration", 
    "price": 32000, 
    "description": "Charming Resin Decorative Bowl with Smooth Finish", 
    "detaildescription": "A charming decorative bowl made from resin with a smooth, glossy finish. Its versatile design makes it suitable for various uses, from displaying small items to serving snacks.",
    "rating": 4.0, 
    "review": 145, 
    "img": "https://i.ibb.co/gPc78Yb/p4.jpg" 
  },
  { 
    "id": 18, 
    "type": "clock", 
    "price": 55000, 
    "description": "Stylish Resin Wall Clock with Minimalist Design", 
    "detaildescription": "This stylish wall clock features a minimalist resin design, perfect for adding a modern touch to your interior. Its clean lines and subtle design make it a great addition to contemporary spaces.",
    "rating": 4.5, 
    "review": 165, 
    "img": "https://i.ibb.co/CnqzGZx/w13.webp" 
  },
  { 
    "id": 19, 
    "type": "clock", 
    "price": 58000, 
    "description": "Modern Resin Clock with Vibrant Colors", 
    "detaildescription": "A modern wall clock crafted from resin with vibrant colors. This eye-catching piece adds a splash of color to any room and is designed to be both functional and decorative.",
    "rating": 4.0, 
    "review": 150, 
    "img": "https://i.ibb.co/dJ8K4Z8/w14.webp" 
  },
  { 
    "id": 20, 
    "type": "clock", 
    "price": 63000, 
    "description": "Contemporary Resin and Metal Wall Clock", 
    "detaildescription": "This contemporary wall clock combines resin and metal for a unique look. The contrast between the materials adds a sophisticated touch, making it a stylish addition to any modern interior.",
    "rating": 4.5, 
    "review": 175, 
    "img": "https://i.ibb.co/NKLrMD4/w16.webp" 
  },
  { 
    "id": 21, 
    "type": "decoration", 
    "price": 35000, 
    "description": "Colorful Resin Decorative Plate with Artistic Design", 
    "detaildescription": "A colorful decorative plate made from resin, featuring an artistic design. Ideal for adding a pop of color to any space, it can be used as a display piece or for serving.",
    "rating": 4.0, 
    "review": 160, 
    "img": "https://i.ibb.co/V3RJSqt/p9.webp" 
  },
  { 
    "id": 22, 
    "type": "decoration", 
    "price": 30000, 
    "description": "Handcrafted Resin Vase with Unique Patterns", 
    "detaildescription": "This handcrafted resin vase features unique patterns and a striking design. Perfect for displaying flowers or as a standalone piece of art, it adds a touch of elegance to any room.",
    "rating": 4.5, 
    "review": 170, 
    "img": "https://i.ibb.co/YN5rvTh/p10.webp" 
  },
  { 
    "id": 23, 
    "type": "decoration", 
    "price": 28000, 
    "description": "Artistic Resin Wall Hanging with Modern Design", 
    "detaildescription": "An artistic wall hanging made from resin, featuring a modern design that adds a contemporary flair to any space. Its vibrant colors and unique shape make it a standout piece.",
    "rating": 4.0, 
    "review": 140, 
    "img": "https://i.ibb.co/8xm2gHN/p11.webp" 
  },
  { 
    "id": 24, 
    "type": "decoration", 
    "price": 38000, 
    "description": "Elegant Resin Wall Art with Geometric Patterns", 
    "detaildescription": "This elegant wall art features geometric patterns in resin, creating a sophisticated and modern look. Ideal for enhancing the decor of any room with its unique and stylish design.",
    "rating": 4.5, 
    "review": 150, 
    "img": "https://i.ibb.co/k6JyqnM/p12.webp" 
  },
  { 
    "id": 25, 
    "type": "decoration", 
    "price": 68000, 
    "description": "Luxury Resin dragon show peace", 
    "detaildescription": "A piece of artistic wall art made from resin, featuring bold colors and unique patterns. Perfect for adding a vibrant touch to any room.",
    "rating": 4.5, 
    "review": 180, 
    "img": "https://i.ibb.co/gMd7pTT/p13.webp" 
  },
  { 
    "id": 26, 
    "type": "sculpture", 
    "price": 90000, 
    "description": "Abstract Resin Sculpture with Modern Aesthetic", 
    "detaildescription": "An abstract resin sculpture featuring a modern aesthetic. Its unique design and striking appearance make it a perfect centerpiece for contemporary art enthusiasts.",
    "rating": 4.5, 
    "review": 160, 
    "img": "https://i.ibb.co/f0KcMh0/s2.webp" 
  },
  { 
    "id": 27, 
    "type": "sculpture", 
    "price": 88000, 
    "description": "Detailed Resin Animal Sculpture with Realistic Features", 
    "detaildescription": "A detailed resin sculpture of an animal with realistic features. This piece is ideal for collectors and nature lovers who appreciate fine craftsmanship and lifelike representations.",
    "rating": 4.0, 
    "review": 170, 
    "img": "https://i.ibb.co/xq3vtGG/s4.webp" 
  },
  { 
    "id": 28, 
    "type": "sculpture", 
    "price": 85000, 
    "description": "Modern Resin Sculpture with Innovative Design", 
    "detaildescription": "A modern resin sculpture featuring an innovative design. Its cutting-edge look and contemporary style make it an eye-catching addition to any modern art collection.",
    "rating": 4.0, 
    "review": 180, 
    "img": "https://i.ibb.co/VCS8v0C/s5.webp" 
  },
  { 
    "id": 29, 
    "type": "sculpture", 
    "price": 82000, 
    "description": "Handcrafted Resin Sculpture with Unique Artistry", 
    "detaildescription": "A handcrafted resin sculpture showcasing unique artistry. Each piece is carefully crafted to capture the essence of fine art, making it a standout addition to any art collection.",
    "rating": 4.5, 
    "review": 150, 
    "img": "https://i.ibb.co/p4gHL5Q/s6.webp" 
  },
  { 
    "id": 30, 
    "type": "sculpture", 
    "price": 77000, 
    "description": "Elegant Resin Sculpture with Sophisticated Design", 
    "detaildescription": "An elegant resin sculpture featuring a sophisticated design. This piece adds a touch of class to any space and is perfect for those who appreciate refined art.",
    "rating": 4.5, 
    "review": 160, 
    "img": "https://i.ibb.co/34m7K0m/s7.webp" 
  },
  { 
    "id": 31, 
    "type": "sculpture", 
    "price": 80000, 
    "description": "Intricate Resin Sculpture with Artistic Flair", 
    "detaildescription": "This intricate resin sculpture is designed with artistic flair, capturing the beauty and complexity of modern art. Ideal for those who appreciate detailed craftsmanship and unique designs.",
    "rating": 4.0, 
    "review": 140, 
    "img": "https://i.ibb.co/stDypLQ/s9.jpg" 
  },
  { 
    "id": 32, 
    "type": "sculpture", 
    "price": 72000, 
    "description": "Classic Resin sculpture of the bird", 
    "detaildescription": "This intricate resin sculpture is designed with artistic flair, capturing the beauty and complexity of modern art. Ideal for those who appreciate detailed craftsmanship and unique designs.",
    "rating": 4.5, 
    "review": 170, 
    "img": "https://i.ibb.co/JH0syK5/s12.jpg" 
  },
  { 
    "id": 33, 
    "type": "clock", 
    "price": 69000, 
    "description": "Modern Resin Clock with Unique Aesthetic", 
    "detaildescription": "A modern resin clock featuring a unique aesthetic. Its contemporary design and eye-catching appearance make it a standout piece for any modern home.",
    "rating": 4.0, 
    "review": 155, 
    "img": "https://i.ibb.co/ScDr11n/w1.webp" 
  },
  { 
    "id": 34, 
    "type": "clock", 
    "price": 60000, 
    "description": "Elegant Resin Clock with Sleek Design", 
    "detaildescription": "This elegant clock features a sleek resin design, making it a perfect addition to any sophisticated interior. Its understated elegance adds a touch of class to any room.",
    "rating": 4.5, 
    "review": 145, 
    "img": "https://i.ibb.co/SyrBqyY/w3.webp" 
  },
  { 
    "id": 35, 
    "type": "clock", 
    "price": 66000, 
    "description": "Contemporary Resin Wall Clock with Clean Lines", 
    "detaildescription": "A contemporary wall clock made from resin with clean lines. Its modern design and high-quality finish make it a perfect choice for adding a touch of style to any contemporary setting.",
    "rating": 4.5, 
    "review": 160, 
    "img": "https://i.ibb.co/yQcvkWH/w5.jpg" 
  },
  { 
    "id": 36, 
    "type": "clock", 
    "price": 64000, 
    "description": "Stylish Resin Clock with Minimalist Approach", 
    "detaildescription": "This stylish clock features a minimalist design, crafted from resin. Its simple yet elegant look makes it a versatile addition to various interior styles.",
    "rating": 4.0, 
    "review": 150, 
    "img": "https://i.ibb.co/hdrYKtF/w6.jpg" 
  },
  { 
    "id": 37, 
    "type": "clock", 
    "price": 70000, 
    "description": "Sleek Resin Wall Clock with Modern Appeal", 
    "detaildescription": "A sleek wall clock with a modern resin finish. Its appealing design and refined look make it an excellent choice for contemporary interiors.",
    "rating": 4.5, 
    "review": 175, 
    "img": "https://i.ibb.co/FbdkxHH/w7.jpg" 
  },
  { 
    "id": 38, 
    "type": "clock", 
    "price": 67000, 
    "description": "Resin Wall Clock with Elegant Gold Accents", 
    "detaildescription": "This wall clock features resin construction with elegant gold accents. Its sophisticated design adds a luxurious touch to any room.",
    "rating": 4.5, 
    "review": 180, 
    "img": "https://i.ibb.co/DtB91PM/w8.webp" 
  },
  { 
    "id": 39, 
    "type": "clock", 
    "price": 61000, 
    "description": "Contemporary Resin Clock with Artistic Design", 
    "detaildescription": "A contemporary clock with an artistic resin design. This unique piece adds a modern flair to any interior while providing functionality.",
    "rating": 4.0, 
    "review": 160, 
    "img": "https://i.ibb.co/0Q6Dchr/w9.jpg" 
  },
  { 
    "id": 40, 
    "type": "clock", 
    "price": 62000, 
    "description": "Resin Clock with Modern and Elegant Finish", 
    "detaildescription": "This resin clock combines modern design with an elegant finish. It is ideal for adding a touch of sophistication to any contemporary space.",
    "rating": 4.5, 
    "review": 155, 
    "img": "https://i.ibb.co/pJtHBv3/w10.jpg" 
  },
  { 
    "id": 41, 
    "type": "clock", 
    "price": 59000, 
    "description": "Modern Resin Clock with Unique Shape", 
    "detaildescription": "A modern clock with a unique resin shape. Its distinctive design makes it a standout piece, perfect for adding character to any modern room.",
    "rating": 4.0, 
    "review": 145, 
    "img": "https://i.ibb.co/HGsgfDz/w11.jpg" 
  },
  { 
    "id": 42, 
    "type": "clock", 
    "price": 57000, 
    "description": "Elegant Resin Clock with Timeless Design", 
    "detaildescription": "This elegant resin clock features a timeless design. Its classic look and high-quality finish make it a versatile piece for various interior styles.",
    "rating": 4.5, 
    "review": 150, 
    "img": "https://i.ibb.co/2vXGT9x/w12.jpg" 
  },
  { 
    "id": 43, 
    "type": "decoration", 
    "price": 36000, 
    "description": "Artistic Resin Wall Art with Bold Colors", 
    "detaildescription": "A piece of artistic wall art made from resin, featuring bold colors and unique patterns. Perfect for adding a vibrant touch to any room.",
    "rating": 4.5, 
    "review": 160, 
    "img": "https://i.ibb.co/Jvhc5jh/p6.jpg" 
  },
  { 
    "id": 44, 
    "type": "decoration", 
    "price": 34000, 
    "description": "Chic Resin Decorative Wall Panel", 
    "detaildescription": "This chic decorative wall panel made from resin adds a touch of sophistication to any space. Its elegant design and high-quality finish make it a standout piece.",
    "rating": 4.0, 
    "review": 150, 
    "img": "https://i.ibb.co/dJ8K4Z8/w14.webp" 
  },
  { 
    "id": 45, 
    "type": "decoration", 
    "price": 33000, 
    "description": "Modern Resin Wall Hanging with Abstract Design", 
    "detaildescription": "A modern wall hanging crafted from resin with an abstract design. Its contemporary look and vibrant colors make it a perfect choice for modern decor.",
    "rating": 4.5, 
    "review": 165, 
    "img": "https://i.ibb.co/5B6Xt6c/p8.jpg" 
  },
  { 
    "id": 46, 
    "type": "decoration", 
    "price": 60000, 
    "description": "Sleek Resin Wall Clock with Minimalist Design", 
    "detaildescription": "A sleek and minimalist wall clock made from resin. Its clean design and modern appeal make it a perfect addition to any contemporary space.",
    "rating": 4.5, 
    "review": 170, 
    "img": "https://i.ibb.co/NKLrMD4/w16.webp" 
  }       
        
    ]

    # Create Product instances and save them to the database
    products = [
        Product(
            id=product['id'],
            type=product['type'],
            price=product['price'],
            description=product['description'],
            detaildescription=product['detaildescription'],
            rating=product['rating'],
            review=product['review'],
            img=product['img']
        )
        for product in ProductsData
    ]

    # Bulk create all products in a single query
    Product.objects.bulk_create(products)

    return HttpResponse("Multiple products successfully added!")
