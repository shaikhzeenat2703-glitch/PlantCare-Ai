import re


# ==========================================
# PLANTCARE AI - FREE CHATBOT
# No API / No payment required
# ==========================================


# ---------- LANGUAGE DETECTION ----------

def detect_language(message, selected_language="en"):

    text = message.lower()

    hindi_words = [
        "kya", "hai", "hain", "kaise", "kaisa", "kyu", "kyun",
        "mera", "meri", "mere", "plant", "poudha", "paudha",
        "paani", "pani", "patta", "patte", "bimari", "ilaj",
        "ilaaj", "karo", "karu", "ho", "raha", "rhi", "rhi",
        "chahiye", "kitna", "kab", "kyun"
    ]

    marathi_words = [
        "kay", "kaay", "ahe", "aahe", "kase", "kashi", "ka",
        "maza", "mazi", "mazya", "zhad", "paan", "paani",
        "rog", "upay", "karaycha", "karaychi", "kiti",
        "kuthe", "kaay", "hav"
    ]

    hindi_count = sum(word in text for word in hindi_words)
    marathi_count = sum(word in text for word in marathi_words)

    if marathi_count > hindi_count and marathi_count > 0:
        return "mr"

    if hindi_count > 0:
        return "hi"

    return selected_language


# ---------- CLEAN TEXT ----------

def clean_text(message):

    message = message.lower()

    message = re.sub(r"[^\w\s]", " ", message)

    message = re.sub(r"\s+", " ", message)

    return message.strip()


# ---------- HELPER ----------

def contains_any(text, words):

    return any(word in text for word in words)


# ---------- MAIN CHATBOT ----------

def get_chatbot_response(message, language="en"):

    if not message:
        return "Please type a question about plants."

    text = clean_text(message)

    detected_language = detect_language(
        text,
        language
    )

    # ==========================================
    # ENGLISH
    # ==========================================

    if detected_language == "en":

        # Greeting
        if contains_any(text, [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]):
            return (
                "Hello! 🌱 I am PlantCare AI. "
                "You can ask me about plant diseases, "
                "plant care, watering, leaves, tomatoes, "
                "potatoes, peppers and more."
            )

        # Diseases
        if contains_any(text, [
            "what diseases",
            "plant diseases",
            "diseases can plants",
            "common diseases",
            "plant disease",
            "disease can",
            "diseases are"
        ]):
            return (
                "Plants can have many diseases. 🌱 Common examples include "
                "bacterial spot, early blight, late blight, leaf mold, "
                "septoria leaf spot, target spot, mosaic virus and "
                "yellow leaf curl virus. Plants can also have problems "
                "such as spider mites and nutrient deficiencies. "
                "You can upload a clear leaf image in the Detect Disease "
                "section for an AI-based prediction."
            )

        # Tomato
        if contains_any(text, [
            "tomato",
            "tomato plant",
            "tomato leaves"
        ]):
            return (
                "Tomato plants can suffer from bacterial spot, early blight, "
                "late blight, leaf mold, septoria leaf spot, target spot, "
                "spider mites, yellow leaf curl virus and mosaic virus. 🍅 "
                "Keep the leaves dry, provide good air circulation and "
                "avoid unnecessary overhead watering."
            )

        # Potato
        if contains_any(text, [
            "potato",
            "potato plant",
            "potato leaves"
        ]):
            return (
                "Potato plants commonly face early blight and late blight. 🥔 "
                "Remove badly affected leaves, avoid excess moisture on leaves, "
                "provide good air circulation and keep the growing area clean."
            )

        # Pepper
        if contains_any(text, [
            "pepper",
            "capsicum",
            "bell pepper"
        ]):
            return (
                "Pepper plants can develop bacterial spot and other leaf problems. "
                "Keep foliage dry, avoid overcrowding, remove badly affected "
                "plant material and maintain good garden hygiene."
            )

        # Water
        if contains_any(text, [
            "water",
            "watering",
            "how much water",
            "how often water",
            "paani"
        ]):
            return (
                "Watering depends on the plant, soil and weather. 💧 "
                "Generally, water when the top layer of soil becomes dry. "
                "Avoid keeping the soil continuously waterlogged."
            )

        # Yellow leaves
        if contains_any(text, [
            "yellow leaves",
            "yellow leaf",
            "leaves are yellow",
            "leaf is yellow",
            "leaves turning yellow"
        ]):
            return (
                "Yellow leaves can have several causes, including overwatering, "
                "underwatering, nutrient deficiency, pests or disease. 🌿 "
                "Check the soil moisture, inspect the underside of leaves "
                "for pests and look for spots or unusual patterns."
            )

        # White spots
        if contains_any(text, [
            "white spots",
            "white spot",
            "white powder",
            "white patches"
        ]):
            return (
                "White spots or powder on leaves may be related to fungal "
                "problems or pests. 🔍 Check both sides of the leaf carefully. "
                "A clear photo can help identify the problem more accurately."
            )

        # Brown spots
        if contains_any(text, [
            "brown spots",
            "brown spot",
            "brown leaves",
            "black spots",
            "black spot"
        ]):
            return (
                "Brown or black spots can occur because of fungal or bacterial "
                "diseases, pests, watering problems or leaf damage. 🌱 "
                "Avoid wetting the leaves unnecessarily and inspect the "
                "affected area closely."
            )

        # Plant care
        if contains_any(text, [
            "plant care",
            "care for plant",
            "take care",
            "how to care",
            "care of plant",
            "plant ko care"
        ]):
            return (
                "Basic plant care includes proper sunlight, suitable watering, "
                "well-draining soil, enough nutrients and regular inspection "
                "for pests or diseases. 🌿 Remove severely damaged leaves "
                "when appropriate."
            )

        # Healthy plant
        if contains_any(text, [
            "healthy plant",
            "keep plant healthy",
            "plant healthy",
            "healthy plants"
        ]):
            return (
                "To keep a plant healthy 🌱, provide suitable sunlight, "
                "water according to soil moisture, use well-draining soil, "
                "give appropriate nutrients and regularly check leaves "
                "for pests and diseases."
            )

        # Diagnosis
        if contains_any(text, [
            "diagnose",
            "diagnosis",
            "what disease does my plant have",
            "what disease is my plant",
            "my plant is sick",
            "plant is sick"
        ]):
            return (
                "I can help you understand possible plant problems, but text "
                "alone cannot confirm a disease. 🌱 For a better prediction, "
                "upload a clear photo of the affected leaf using the "
                "Detect Disease section."
            )

        # General plant questions
        if contains_any(text, [
            "plant",
            "leaf",
            "leaves",
            "soil",
            "garden",
            "gardening",
            "seed",
            "fertilizer",
            "fertiliser",
            "pest",
            "insect",
            "root",
            "stem",
            "flower",
            "grow"
        ]):
            return (
                "Sure! 🌱 I can help with plant diseases, leaves, watering, "
                "soil, pests, fertilizers, plant care and common problems. "
                "Tell me what is happening with your plant."
            )

        # Unrelated question
        return (
            "I am PlantCare AI 🌱 and I am designed to answer "
            "plant-related questions. Please ask me about plants, "
            "plant diseases, leaves, watering, soil, pests or plant care."
        )


    # ==========================================
    # HINDI
    # ==========================================

    if detected_language == "hi":

        # Greeting
        if contains_any(text, [
            "hello",
            "hi",
            "hey",
            "namaste",
            "namaskar"
        ]):
            return (
                "नमस्ते! 🌱 मैं PlantCare AI हूँ। "
                "आप मुझसे पौधों की बीमारी, देखभाल, पानी, पत्तियों, "
                "टमाटर, आलू, मिर्च और अन्य पौधों से जुड़े सवाल पूछ सकते हैं।"
            )

        # Diseases
        if contains_any(text, [
            "plant ko kya kya disease",
            "plant ki kya kya bimari",
            "kaunsi bimari",
            "konsi bimari",
            "bimari ho sakti",
            "paudhe ki bimari",
            "poudhe ki bimari",
            "plant ki bimari"
        ]):
            return (
                "पौधों में कई तरह की बीमारियाँ हो सकती हैं। 🌱 "
                "जैसे bacterial spot, early blight, late blight, "
                "leaf mold, septoria leaf spot, target spot, "
                "mosaic virus और yellow leaf curl virus। "
                "कुछ समस्याएँ pests और nutrient deficiency के कारण भी होती हैं। "
                "आप Detect Disease section में पत्ती की साफ फोटो upload करके "
                "AI prediction ले सकते हैं।"
            )

        # Tomato
        if contains_any(text, [
            "tomato",
            "tamatar",
            "tamatar ke plant",
            "tomato plant",
            "tomato ke patte"
        ]):
            return (
                "टमाटर के पौधे में bacterial spot, early blight, late blight, "
                "leaf mold, septoria leaf spot, target spot, spider mites, "
                "yellow leaf curl virus और mosaic virus जैसी समस्याएँ हो सकती हैं। 🍅 "
                "पत्तियों को अनावश्यक रूप से गीला न रखें और पौधे के आसपास "
                "अच्छी हवा का प्रवाह रखें।"
            )

        # Potato
        if contains_any(text, [
            "potato",
            "aloo",
            "aloo ke plant",
            "potato plant"
        ]):
            return (
                "आलू के पौधों में early blight और late blight आम समस्याएँ हैं। 🥔 "
                "बहुत ज्यादा प्रभावित पत्तियों को हटाएँ, पत्तियों पर ज्यादा "
                "पानी न डालें और पौधे के आसपास सफाई रखें।"
            )

        # Pepper
        if contains_any(text, [
            "pepper",
            "capsicum",
            "shimla mirch",
            "mirchi",
            "mirch"
        ]):
            return (
                "मिर्च या शिमला मिर्च के पौधों में bacterial spot जैसी बीमारी "
                "हो सकती है। 🌶️ पत्तियों को सूखा रखने की कोशिश करें, "
                "पौधों में पर्याप्त दूरी रखें और प्रभावित हिस्सों पर ध्यान दें।"
            )

        # Water
        if contains_any(text, [
            "paani",
            "pani",
            "kitna paani",
            "kitna pani",
            "paani kitna",
            "pani kitna",
            "paani dena",
            "pani dena"
        ]):
            return (
                "पौधे को कितना पानी देना है यह पौधे, मिट्टी और मौसम पर निर्भर करता है। 💧 "
                "आमतौर पर जब मिट्टी की ऊपरी परत सूखी लगे तब पानी दें। "
                "मिट्टी को लगातार बहुत ज्यादा गीला न रखें।"
            )

        # Yellow leaves
        if contains_any(text, [
            "patte yellow",
            "patta yellow",
            "patte peele",
            "patta peela",
            "patte peele ho",
            "leaves yellow",
            "leaves peeli"
        ]):
            return (
                "पत्तियाँ पीली होने के कई कारण हो सकते हैं, जैसे ज्यादा पानी, "
                "कम पानी, nutrient deficiency, pests या बीमारी। 🌿 "
                "मिट्टी की नमी देखें और पत्तियों के नीचे pests को भी check करें।"
            )

        # White spots
        if contains_any(text, [
            "white spots",
            "white spot",
            "safed daag",
            "safed nishan",
            "white powder"
        ]):
            return (
                "पत्तियों पर सफेद दाग या powder जैसी परत fungal problem या "
                "pests से जुड़ी हो सकती है। 🔍 पत्ती के दोनों तरफ ध्यान से देखें। "
                "साफ फोटो upload करने से समस्या पहचानने में ज्यादा मदद मिल सकती है।"
            )

        # Brown spots
        if contains_any(text, [
            "brown spots",
            "brown spot",
            "bhure daag",
            "kale daag",
            "black spots",
            "black spot"
        ]):
            return (
                "भूरे या काले दाग fungal या bacterial disease, pests, "
                "पानी की समस्या या leaf damage के कारण हो सकते हैं। 🌱 "
                "पत्तियों को अनावश्यक रूप से गीला न रखें और प्रभावित हिस्से को ध्यान से देखें।"
            )

        # Care
        if contains_any(text, [
            "plant ki care",
            "paudhe ki care",
            "poudhe ki care",
            "plant kaise healthy",
            "plant ko healthy",
            "paudhe ko healthy",
            "plant ki dekhbhal",
            "paudhe ki dekhbhal"
        ]):
            return (
                "पौधे की अच्छी देखभाल के लिए सही sunlight, जरूरत के अनुसार पानी, "
                "अच्छी drainage वाली मिट्टी और सही nutrients जरूरी हैं। 🌱 "
                "पत्तियों को नियमित रूप से pests और diseases के लिए check करें।"
            )

        # Diagnosis
        if contains_any(text, [
            "plant ko kya hua",
            "paudhe ko kya hua",
            "poudhe ko kya hua",
            "plant mein bimari",
            "paudhe mein bimari",
            "plant sick",
            "plant kharab"
        ]):
            return (
                "सिर्फ text से बीमारी को पूरी तरह confirm करना मुश्किल है। 🌱 "
                "आप affected leaf की साफ फोटो Detect Disease section में upload करें। "
                "हमारा disease detection model उस image के आधार पर prediction देगा।"
            )

        # General plant
        if contains_any(text, [
            "plant",
            "paudha",
            "poudha",
            "patta",
            "patte",
            "mitti",
            "garden",
            "bagicha",
            "khaad",
            "fertilizer",
            "pest",
            "keeda"
        ]):
            return (
                "हाँ 🌱 मैं पौधों से जुड़े सवालों में मदद कर सकता हूँ। "
                "आप बीमारी, पत्तियाँ, पानी, मिट्टी, pests, fertilizer या "
                "plant care के बारे में पूछ सकते हैं।"
            )

        return (
            "मैं PlantCare AI हूँ 🌱 और मेरा focus पौधों से जुड़े सवालों पर है। "
            "आप plant disease, leaves, पानी, मिट्टी, pests या plant care के बारे में पूछें।"
        )


    # ==========================================
    # MARATHI
    # ==========================================

    if detected_language == "mr":

        if contains_any(text, [
            "hello",
            "hi",
            "namaskar",
            "namaste"
        ]):
            return (
                "नमस्कार! 🌱 मी PlantCare AI आहे. "
                "तुम्ही मला झाडांचे रोग, काळजी, पाणी, पाने, "
                "टोमॅटो, बटाटा आणि मिरची याबद्दल प्रश्न विचारू शकता."
            )

        if contains_any(text, [
            "zhadala konta rog",
            "zhadache rog",
            "zhadanna rog",
            "rog hou shakto",
            "kontya rog",
            "paananna rog"
        ]):
            return (
                "झाडांना अनेक प्रकारचे रोग होऊ शकतात. 🌱 "
                "उदाहरणार्थ bacterial spot, early blight, late blight, "
                "leaf mold, septoria leaf spot, target spot, "
                "mosaic virus आणि yellow leaf curl virus. "
                "काही समस्या pests किंवा nutrients च्या कमतरतेमुळेही होऊ शकतात."
            )

        if contains_any(text, [
            "tomato",
            "tomato plant",
            "tomato chi paane",
            "tomato che paan"
        ]):
            return (
                "टोमॅटोच्या झाडाला bacterial spot, early blight, late blight, "
                "leaf mold, septoria leaf spot, target spot आणि काही viral "
                "समस्या होऊ शकतात. 🍅 झाडाभोवती हवा खेळती ठेवा आणि पाने "
                "अनावश्यकपणे ओलसर ठेवू नका."
            )

        if contains_any(text, [
            "potato",
            "batata",
            "batatyache zhad",
            "batatyachi paane"
        ]):
            return (
                "बटाट्याच्या झाडाला early blight आणि late blight सारखे रोग होऊ शकतात. 🥔 "
                "जास्त प्रभावित पाने काढा, पानांवर जास्त पाणी टाकू नका आणि "
                "झाडाभोवती स्वच्छता ठेवा."
            )

        if contains_any(text, [
            "pepper",
            "mirchi",
            "mirch",
            "shimla mirchi"
        ]):
            return (
                "मिरची किंवा शिमला मिरचीच्या झाडाला bacterial spot सारखे रोग होऊ शकतात. 🌶️ "
                "पाने कोरडी ठेवण्याचा प्रयत्न करा आणि झाडांमध्ये योग्य अंतर ठेवा."
            )

        if contains_any(text, [
            "paani",
            "pani",
            "kiti paani",
            "paani kiti",
            "pani kiti"
        ]):
            return (
                "झाडाला किती पाणी द्यायचे हे झाड, माती आणि हवामानावर अवलंबून असते. 💧 "
                "मातीचा वरचा थर कोरडा वाटल्यावर साधारणपणे पाणी द्या. "
                "माती सतत खूप ओलसर ठेवू नका."
            )

        if contains_any(text, [
            "paane pivali",
            "paan pivale",
            "yellow leaves",
            "yellow leaf"
        ]):
            return (
                "पाने पिवळी होण्याची अनेक कारणे असू शकतात, जसे जास्त पाणी, "
                "कमी पाणी, nutrients ची कमतरता, pests किंवा रोग. 🌿 "
                "मातीतील ओलावा आणि पानांच्या खालील भाग तपासा."
            )

        if contains_any(text, [
            "paanavar daag",
            "pandhare daag",
            "white spots",
            "brown spots",
            "kale daag"
        ]):
            return (
                "पानांवरील डाग fungal किंवा bacterial समस्या, pests किंवा "
                "पाण्याशी संबंधित समस्यांमुळे होऊ शकतात. 🔍 "
                "पानाचा स्पष्ट फोटो upload केल्यास समस्या ओळखण्यास मदत होईल."
            )

        if contains_any(text, [
            "zhadachi kalaji",
            "plant care",
            "zhad healthy",
            "plant healthy",
            "kalaji kashi"
        ]):
            return (
                "झाडाची चांगली काळजी घेण्यासाठी योग्य sunlight, योग्य प्रमाणात "
                "पाणी, चांगला drainage असलेली माती आणि योग्य nutrients आवश्यक आहेत. 🌱 "
                "पाने नियमितपणे pests आणि रोगांसाठी तपासा."
            )

        if contains_any(text, [
            "zhadala kay zale",
            "zhadala kay zala",
            "rog aahe",
            "rog ahe",
            "zhad kharab"
        ]):
            return (
                "फक्त text वरून रोग निश्चित करणे कठीण आहे. 🌱 "
                "Affected leaf चा स्पष्ट फोटो Detect Disease section मध्ये upload करा. "
                "Disease detection model image वरून prediction देईल."
            )

        if contains_any(text, [
            "zhad",
            "paan",
            "paane",
            "mati",
            "bag",
            "sheti",
            "khat",
            "pest",
            "keede"
        ]):
            return (
                "हो 🌱 मी झाडांशी संबंधित प्रश्नांमध्ये मदत करू शकतो. "
                "तुम्ही रोग, पाने, पाणी, माती, pests, fertilizer किंवा "
                "झाडांची काळजी याबद्दल विचारू शकता."
            )

        return (
            "मी PlantCare AI आहे 🌱 आणि माझा focus झाडांशी संबंधित प्रश्नांवर आहे. "
            "कृपया plant disease, पाने, पाणी, माती, pests किंवा plant care बद्दल विचारा."
        )


    # ---------- FINAL FALLBACK ----------

    return (
        "I can help with plant-related questions. 🌱"
    )