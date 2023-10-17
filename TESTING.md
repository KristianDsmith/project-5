# TESTING

## Manual Testing

Testing was done throughout site development, for each feature before it was merged into the master file.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.

![Sign Up](documentation/signup.png)

![Login](documentation/login.png)

![Navigation](documentation/navigation.png)

![Product](documentation/product.png)

![Checkout](documentation/checkout.png)


## Testing User Story

| Shopper Goals | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a shopper I can view all list of products so that select some to purchase | Y | ![Products](documentation/user-1.png) |
| As a shopper I can view a specific category of products so that quickly find products i am interested in. | Y | ![Products](documentation/user-2.png) |
| As a shopper I can view individual product details so that identify price, description, product rating, product image, listen to sample music, available sizes | Y | ![Product Detail](documentation/user-3.png) |
|As a First Time Visitor, I want to be able to find the app useful, so that I can use it according to my needs. | Y | ![Benefits](documentation/features/home/about_us_section_1.png) ![Benefits](documentation/features/home/about_section_2.png)|
| As a First Time Visitor, I want to be informed clearly if I am making any errors when registering my account, so that I can be able to fix any errors quickly if I make some. | Y | ![Signup Page](documentation/features/allauth_access/sign_up.png) |
| As a First Time Visitor, I want to be able to see the list of products, so that I can learn the benefits of the app as a user. | Y | ![Products](documentation/features/store/store_page.png) |

| Frequent Visitor Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Regular User, I want to be able to access my account without having to log in every time, so that I can quickly buy a product that I need. | Y | ![Login Page](documentation/features/allauth_access/login.png) |
| As a Regular User, I want to be sure that my account details are protected, so that I can safely make purchases. | Y | ![Login Page](documentation/features/footer/footer.png) |
| As a Regular User, I want to be able to view my data, so that I can easily check my account details and past orders. | Y | ![My Orders](documentation/features/my_orders/my_orders_page.png) |
| As a Regular User, I want to be able to add, edit, and save my address data, so that I can make an order faster. | Y | ![My addresses](documentation/features/my_addresses/my_addresses_page.png) |
| As a Regular User, I want to be able to search products by category, tag, or text search, so that I can find a product faster., s a Regular User, I want to be able to sort products by category, so that I can find the best option to buy. | Y | ![Store Search](documentation/features/store/store_search_bar.png) |
| As a Regular User, I want to be able to leave a product review, so that I can share my feedback. | Y | ![Add Review](documentation/features/my_order_details/my_order_details_completed_order.png) |
| As a Regular Visitor, I want to be able to see ratings and reviews on a product, so that I can make a prudent decision before buying it. | Y | ![Ratings and Reviews](documentation/features/product_details/product_rating_reviews.png) |
| As a Regular User, I want to be able to see the list of products, so that I can learn the benefits of the app as a user. | Y | ![Products](documentation/features/store/store_page.png) |
| As a Regular Customer, I want to be able to see discount offers, so that I can buy products with a discount and save some money. | Y | ![Discount Offers](documentation/features/store/store_product_card.png) |
| As a Customer, I want to be able to see if the product is about to go out of stock, so that I can plan my purchases. | Y | ![Product Details](documentation/features/product_details/quantity_warning_msg.png) |
| As a Customer, I want to be able to see if the product is out of stock, so that I can be informed in advance that the item is not available and save my time. | Y | ![Product Details](documentation/features/store/store_products_cards_prices.png) |
| As a Customer, I want to be able to See a full product description (image, name, description, options, price, discount), so that I can understand whether I want to buy this product. | Y | ![Product Details](documentation/features/product_details/product_details_page.png) |
|As a Customer, I want to be able to see the product’s options (size, color, height), so that I can understand whether the option of the product suits me. | Y | ![Product Details](documentation/features/product_details/request_msg_not_displayed.png) |
| As a Customer, I want to be able to choose, edit product’s options (size, color, height), so that I can choose an appropriate option of the product. | Y | ![Product Details](documentation/features/product_details/show_price_on_value_change.png) |
| As a Customer, I want to be able to ask for the notification from the shop if I want to purchase a product that is out of stock or about to finish, so that I can buy a product that I really want. | Y | ![Product Details](documentation/features/product_details/modal_product_request.png) |
| As a Customer, I want to be able to get an email notification from the shop about special offers, promotions, discounts, so that I can make purchases cheaper. | Y | ![Product Details. Newsletter Emails](documentation/web_marketing/newsletter.png) ![Product Details. Promo  Emails](documentation/web_marketing/promo_email.png)|
| As a Customer, I want to be able to get an email notification from the shop if the product that I wanted and was out of stock came back to the shop, so that I can buy a product that I really want when it is available.   | Y | ![Product Details](documentation/features/product_details/stock_answer_email.png) |
| As a Customer, I want to be able to add product to my wish list, so that I can buy it later. | Y | ![Product Details. Adding to wishlist](documentation/features/product_details/adding_to_wishlist.png) ![Product Details](documentation/features/product_details/add_to_wishlist_msg.png) |
| As a Customer, I want to be able to remove products to my wish list, so that I can keep my wish list up to date. | Y |![Product Details](documentation/features/product_details/added_to_wishlist.png) |
| As a Customer, I want to be able to view products on my wish list, so that I can plan my purchases. | Y | ![Product Details](documentation/features/wishlist/wishlist_page.png) |
| As a Customer, I want to be able to add products to my bag, so that I can easily save products in the bag. | Y | ![Product Details](documentation/features/product_details/add_to_bag_button_enable.png) ![Product Details](documentation/features/product_details/add_to_bag_msg.png) |
| As a Customer, I want to be able to increase/reduce the number of product items in my bag that I want, so that I can buy a number of items that I want. | Y | ![Product Details](documentation/features/bag/bag_buttons_quantity_control.png) |
| As a Customer, I want to be able to see the counted total cost of the product, so that I can see how much I will spend. | Y | ![Product Details](documentation/features/bag/bag_table.png) |
| As a Customer, I want to be able to see the total cost of the products in the bag, so that I can see how much I will spend. | Y | ![Product Details](documentation/features/bag/bag_summary.png) |
| As a Customer, I want to be able to remove the product from my bag, so that I can change my mind not to buy a particular product at the last moment. | Y | ![Product Details](documentation/features/bag/bag_buttons_remove_product_from_bag.png) |
| As a Customer, I want to be able to see messages from the shop, so that I can understand whether an item is actually added to the bag or removed.   | Y | ![Product Details](documentation/features/product_details/add_to_bag_msg.png) |
| As a Visitor, I want to be able to send photos of a product, so that I can provide proof if there are any probable issues with the delivered product (wrong color, size, or damage). | Y | ![Product Details](documentation/features/my_review/my_reviews_page.png) |
| As a Customer who made a purchase, I want to be able to review the order status, so that I can understand where my purchase is. | Y | ![Product Details](documentation/features/product_review/product_review_page.png) |
| As a Customer who made a purchase, I want to be able to see order confirmation after checkout, so that I can see what I bought. | Y | ![Product Details](documentation/features/order_placed/order_placed_page.png) |
| As a Customer who made a purchase, I want to be able to receive an email confirmation of my purchase, so that I can have email proof of purchase. | Y | ![Product Details](documentation/features/payment/payment_confirmation_email.png) |
| As a Regular user, I want to be able to change my profile data, so that I can keep my profile up to date. | Y | ![Product Details](documentation/features/edit_profile/edit_profile_page.png) |
| As a Regular User, I want to be able to add, edit, and delete addresses, so that I can be sure that I will receive my order at the correct address. | Y | ![My Addresses](documentation/features/my_addresses/my_addresses_page.png) ![Add address](documentation/features/my_addresses/my_addresses_page.png) ![Edit address](documentation/features/my_addresses/add_new_address_button.png) ![Edit address](documentation/features/edit_address/edit_address_form.png) |
| As a Regular User, I want to be able to change primary address, so that I can set the primary address without editing it. | Y | ![My Addresses](documentation/features/my_addresses/my_addresses_page.png) ![Edit address](documentation/features/my_addresses/address_card_not_primary.png) ![Edit address](documentation/features/my_addresses/address_card_primary.png) |

| Manager + Admin Visitor Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Manager, I want to be able to add, edit, and delete category, so that I can keep products’ categories up to date. | Y | ![Category](documentation/features/personnel/categories/categories_page.png) |
| As a Manager, I want to be able to add, edit, and delete products, so that I can keep shop products up to date.  | Y | ![Product full heading](documentation/features/personnel/products_table/products_table_heading.png) ![Product full heading](documentation/features/personnel/product_full/product_full_heading.png) |
| As a Manager, I want to be able to add, edit, delete tags, so that I can keep products’ sorting up to date and, as a result, increase sales.  | Y | ![Personnel Tags](documentation/features/personnel/tags/tags_page.png) ![Personnel tag details](documentation/features/personnel/tags/tag_detail.png) |
| As a Manager, I want to be able to change tags for a product, so that I can increase sales for a particular product.  | Y | ![Personnel Product full edit](documentation/features/personnel/product_full/edit_product.png) |
| As a Manager, I want to be able to Add, edit, and delete products’ options (attributes and values), so that I can keep products’ options up to date. | Y | ![Personnel Product full edit](documentation/features/personnel/product_full/edit_product.png) |
| As a Manager, I want to be able to send emails to customers about future promotions, so that I can increase sales by notifying customers about promotions. | Y | ![Product Details. Newsletter Emails](documentation/web_marketing/newsletter.png) ![Product Details. Promo  Emails](documentation/web_marketing/promo_email.png)|
| As a Manager, I want to be able to view customers' data, so that I can contact customers if needed and solve possible problems with purchases.  | Y | ![Personnel Order Details](documentation/features/personnel/orders/order_full_details_customer_data.png) |
| As a Manager, I want to be able to control product status (active/not active), so that I can keep shop stock up to date.  | Y | ![Personnel Product Stock](documentation/features/personnel/stock/update_stock.png) |
| As a Manager, I want to be able to Review user’s requests on a product that is out of stock, so that I can understand customers' urgent needs. As a Manager, I want to be able to review user’s requests on a product that is about to go out of stock, so that I can understand customers' urgent needs and products’ popularity. | Y | ![Personnel Product Stock](documentation/features/personnel/stock_requests/stock_requests.png) |
| As a Manager, I want to be able to send emails to customers who left notification letters about products coming back to the shop, so that I can enhance customer loyalty and increase sales.  | Y | ![Personnel Product Stock](documentation/features/product_details/stock_answer_email.png) |
| As a Admin, I want to be able to review and edit orders’ status, so that I can control customers’ orders and sales.  | Y | ![Personnel Order Details](documentation/features/personnel/orders/order_full_detail_admin.png) |
| As a Manager, I want to be able to sort products by stock number, so that I can control stock numbers.  | Y | ![Personnel Product Stock](documentation/features/personnel/stock_table/stock_table_select_bar.png) |
| As a Manager, I want to be able to review customers’ orders, so that I can control orders.  | Y | ![Personnel Order Details](documentation/features/personnel/orders/orders_page.png) |
| As a Manager, I want to be able to sort orders by date and status, so that I can prioritize orders.  | Y | ![Personnel Order Details](documentation/features/personnel/orders/orders_bar.png) |
 As a Manager, I want to be able to display new products label, so that I can be sure that customers will be aware of new products in the shop.  | Y | ![Personnel Product Stock](documentation/features/store/store_product_card.png) |
| As a Manager, I want to be able to Allow customers to leave reviews only after they receive a product, so that I can control that reviews are relevant.  | Y | ![Personnel Product Stock](documentation/features/my_order_details/my_order_detail_page.png) |

| Logistics Manager + Admin Visitor Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Logistics Manager or Admin, I want to be able to render order status, so that I can track at which stage the order is in.  | Y | ![Personnel Order Details](documentation/features/personnel/orders/order_status_update.png) |

| Admin Visitor Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As an Admin, I want to be able to add promotions, so that I can increase sales and enhance customers’ loyalty.  | Y |  ![Promotions](documentation/features/personnel/add_promotion/add_promotion_page.png) |
| As an Admin, I want to be able to get a visible notice about products that are running in stock, so that I can keep stock up to date. | Y | ![Product Details. Stock Select](documentation/features/personnel/stock_table/stock_table_selected_fewer_than_20.png) ![Product Details full. Units in stock](documentation/features/personnel/product_full/units_cards_stock.png) |
|  As an Admin, I want to be able to be aware of units sold, so that I can be aware of sales on a particular product. | Y | ![Product Details. Units in stock](documentation/features/personnel/units/unit_card.png) |
| As an Admin, I want to be able to get a visible notice if there is some inconsistency in sales, so that I can be aware of possible stealing.  | Y | ![Product Details. Units in stock](documentation/features/personnel/units/stock_inconsistency.png) |
| As an Admin, I want to be able to get a visible notice if there a product is not salable, so that I can make a decision about stopping purchasing this product for my store.  | Y | ![Product Details. Units in stock](documentation/features/personnel/stock_table/stock_table_select_bar.png) |
|  As an Admin, I want to be able to send special discounts email notifications, so that I can inform loyal customers about special offers. | Y | ![Product Details. Promo  Emails](documentation/web_marketing/promo_email.png)|

---
