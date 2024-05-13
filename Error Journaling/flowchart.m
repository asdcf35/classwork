flowchart

    start(()) --> clear(clear the terminal)
    clear --> console(create console object)
    console --> restaurantFilenames(store all filenames for restaurant menus in a list called restaurant_files)
    restaurantFilenames --> locations(store all locations in a tuple called locations)
    locations --> restaurantObjects(make and empty dictionary, store it to a variable named restaurants)
    restaurantObjects --> lastInRestaurantFiles(is this the last item in restaurant files)
    lastInRestaurantFiles --> |Yes|printAllRestaurantsAndLocations(print all restaurants and locations in this format: 'Index of Restaurant+1 Restaurant Name - Location')
    printAllRestaurantsAndLocations --> numberForNavigation(ask the user for a number)
    numberForNavigation --> checkNumberForNavigation{is number 'q' or a number}
    checkNumberForNavigation -->|Yes| isNumberQ{Is the number q}
    isNumberQ -->|no|isNumberLowerThanHighestIndex(is number lower than the highest index in the dictionary restaurants)
    isNumberLowerThanHighestIndex -->|yes| selectRestaurant(find the restaurant in restaurants using the name found in the keys of restaurant at index number)
    selectRestaurant --> printTheDescription(print the menu of that restaurant)
    printTheDescription --> printQtoReturnRestaurants(print 'hit q to return back')
    printQtoReturnRestaurants --> waitForQtoRestaurants(that's actually awesome)
    wairForQtoRestaurant --> console
    
    %% the loop
    lastInRestaurantFiles -->|No|createRestaurantAtCurrentIndex
    createRestaurantAtCurrentIndex --> lastInRestaurantFiles
    