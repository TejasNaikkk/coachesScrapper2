from souper import souper

def getName(soup):
    h1 = soup.find('h1', class_ = 'elementor-heading-title elementor-size-default')
    return (h1.text)

def getContacts(contact):
    # Address
    addressParent = contact.find('div', class_='elementor-element elementor-element-bc55ad1 elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box')
    address = addressParent.find('h3').text
    
    phone = 'Null'
    website = 'Null'
    email = 'Null'
    facebook = 'Null'
    instagram = 'Null'
    linkedin = 'Null'
    podcast = 'Null'

    # Phone
    try:
        phoneParent = contact.find('div', class_ = 'elementor-element elementor-element-2fb4a52 elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial dc-has-condition dc-condition-empty elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box')
        phone = phoneParent.find('h3').text
    except Exception:
        print(Exception)

    # Website
    try:
        websiteParent = contact.find('div', class_ = 'elementor-element elementor-element-7dafc07 elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial dc-has-condition dc-condition-empty elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box')
        a = websiteParent.find('a')
        website = a['href']
    except Exception:
        print(Exception)

    # Email
    try:
        emailParent = contact.find('div', class_ = 'elementor-element elementor-element-bc390ef elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box')
        a = emailParent.find('a')
        email = a['href']
        email = email[len("mailto:"):]
    except Exception:
        print(Exception)
    
    # Facebook
    try:
        facebookParent = contact.find('div', class_ = 'elementor-element elementor-element-2aef968 elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial dc-has-condition dc-condition-empty elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box')
        a = facebookParent.find('a')
        facebook = a['href']
    except Exception:
        print(Exception)

    # Instagram
    try:
        instagramParent = contact.find('div', class_ = 'elementor-element elementor-element-4904109 elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial dc-has-condition dc-condition-empty elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box')
        a = instagramParent.find('a')
        instagram = a['href']
    except Exception:
        print(Exception)

    # LinkedIn
    try:
        linkedinParent = contact.find('div', class_ = 'elementor-element elementor-element-b5d6c38 elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial dc-has-condition dc-condition-empty elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box')
        a = linkedinParent.find('a')
        linkedin = a['href']
    except Exception:
        print(Exception)

    # Podcast
    try:
        podcastParent = contact.find('div', class_ = 'elementor-element elementor-element-7dd310c elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial dc-has-condition dc-condition-empty elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box')
        a = podcastParent.find('a')
        podcast = a['href']
    except Exception:
        print(Exception)

    details = {
        'Address' : address,
        'Phone' : phone,
        'Website' : website,
        'Email' : email,
        'Facebook' : facebook,
        'Instagram' : instagram,
        'LinkedIn' : linkedin,
        'Podcast' : podcast
    }

    return details

def getMore(more):
    specialities = ['Null']
    education = ['Null']
    coachingFormat = ['Null']

    # Specialities
    try:
        specialitiesParent = more.find('div', class_= 'elementor-column elementor-col-25 elementor-inner-column elementor-element elementor-element-3696016')
        spans = specialitiesParent.find_all('span', class_=False)
        for span in spans:
            specs = span.text
            specs = specs.strip()
            specialities.append(specs)
    except Exception:
        print(Exception)
    
    # Education
    try:
        educationParent = more.find('div', class_= 'elementor-column elementor-col-25 elementor-inner-column elementor-element elementor-element-92b9ed8')
        spans = educationParent.find_all('span', class_=False)
        for span in spans:
            eds = span.text
            eds = eds.strip()
            education.append(eds)
    except Exception:
        print(Exception)
        
    # CoachingFormat
    try:
        coachingFormatParent = more.find('div', class_= 'elementor-column elementor-col-25 elementor-inner-column elementor-element elementor-element-bd94025')
        spans = coachingFormatParent.find_all('span', class_=False)
        for span in spans:
            frmt = span.text
            frmt = frmt.strip()
            coachingFormat.append(frmt)
    except Exception:
        print(Exception)

    payload2 = {
        'Specialities' : specialities[1::],
        'Education' : education[1::],
        'Coaching Format' : coachingFormat[1::]
    }
    return payload2

def getInfo(url):
    soup = souper(url)
    contactSoup = soup.find('div', class_='elementor-element elementor-element-e108c96 elementor-widget elementor-widget-heading').parent
    moreSoup = soup.find('div', class_='elementor-column elementor-col-25 elementor-inner-column elementor-element elementor-element-3696016').parent

    # Get information
    name = getName(soup)
    contacts = getContacts(contactSoup)
    more = getMore(moreSoup)

    # Create payload dict to return to main
    payload = {
        'Name' : name 
    }
    payload.update(contacts)
    payload.update(more)

    return payload