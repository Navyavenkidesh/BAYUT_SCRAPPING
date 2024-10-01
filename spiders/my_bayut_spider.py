# # ####### Final Code for both json and csv output#########

# # import scrapy
# # import csv
# # import json
# # from scrapy.exceptions import CloseSpider

# # class MyBayutSpider(scrapy.Spider):
# #     name = "my_bayut_spider"
# #     allowed_domains = ["www.bayut.com"]
# #     start_urls = ["https://www.bayut.com/to-rent/property/dubai/"]

# #     def __init__(self, *args, **kwargs):
# #         """
# #         Initialize the spider and open both CSV and JSON files for writing.
# #         """
# #         super(MyBayutSpider, self).__init__(*args, **kwargs)
        
# #         # CSV file setup
# #         self.output_csv_file = 'bayut_properties1.csv'
# #         self.csv_file = open(self.output_csv_file, 'w', newline='', encoding='utf-8')
# #         self.csv_writer = csv.writer(self.csv_file)
# #         self.csv_writer.writerow(['Field Name', 'Property 1', 'Property 2', 'Property 3', '...'])

# #         # JSON file setup
# #         self.output_json_file = 'bayut_properties2.json'
# #         self.json_file = open(self.output_json_file, 'w', encoding='utf-8')
# #         self.json_file.write('[\n')  # Start the JSON array

# #         # Initialize a counter for the number of crawled properties
# #         self.property_count = 0

# #         # Set the maximum number of properties to extract
# #         self.max_properties = 1500

# #     def parse(self, response):
# #         # Extract product URLs on the current page
# #         product_urls = response.css('a.d40f2294::attr(href)').getall()  
# #         for url in product_urls:
# #             # Stop crawling if the limit is reached
# #             if self.property_count >= self.max_properties:
# #                 raise CloseSpider(reason="Reached 1500 properties")
# #             yield response.follow(url, self.parse_property_details)

# #         # Extract the URL of the next page using the 'a' tag with title="Next"
# #         next_page = response.css('a[title="Next"]::attr(href)').get()

# #         # Follow the next page if available and the limit hasn't been reached
# #         if next_page is not None and self.property_count < self.max_properties:
# #             next_page_url = response.urljoin(next_page)
# #             yield scrapy.Request(next_page_url, callback=self.parse)

# #     def parse_property_details(self, response):
# #         """
# #         Parse individual property pages to extract property details.
# #         """
# #         # Extract property details
# #         price = response.css('span._2d107f6e::text').get().strip() if response.css('span._2d107f6e::text') else 'N/A'
# #         primary_image = response.css('img._4a3dac18::attr(src)').get() if response.css('img._4a3dac18::attr(src)') else 'N/A'
# #         location = response.css('div.e4fd45f0::text').get().strip() if response.css('div.e4fd45f0::text') else 'N/A'
# #         bed_bath_size = response.css('span._140e6903::text').get().strip() if response.css('span._140e6903::text') else 'N/A'
# #         description_parts = response.css('span._3547dac9::text').getall()
# #         description = " ".join([part.strip() for part in description_parts])

# #         type = ", ".join(response.css('span._2fdf7fc5[aria-label="Type"]::text').getall())
# #         purpose = ", ".join(response.css('span._2fdf7fc5[aria-label="Purpose"]::text').getall())
# #         furnishing = ", ".join(response.css('span._2fdf7fc5[aria-label="Furnishing"]::text').getall())
# #         added_on = ", ".join(response.css('span._2fdf7fc5[aria-label="Reactivated date"]::text').getall())
# #         property_id = ", ".join(response.css('span._2fdf7fc5[aria-label="Reference"]::text').getall())
# #         agent = response.css('span._64aa14db a._1264833a::text').getall()

# #         # Check if the first selector returned any results
# #         if not agent:  # If agent is empty
# #             agent = response.css('span._4c376836.undefined a.d2d04ff3::text').getall()

# #         agent = [name.strip() for name in agent if name.strip()]
# #         permit_number = response.css('span.e56292b8[aria-label="Permit Number"]::text').getall()
# #         amenities = response.css('div._1c78af3b + div._117b341a span._7181e5ac::text').getall()
# #         amenities = [amenity.strip() for amenity in amenities]

# #         breadcrumbs = response.css('div.e28fea44 a._43ad44d9::text').getall()
# #         breadcrumbs = [breadcrumb.strip() for breadcrumb in breadcrumbs if breadcrumb.strip()]

# #         # Organize property details in dictionary
# #         property_details = {
# #             'Property ID': property_id,
# #             'Property URL': response.url,
# #             'Purpose': purpose,
# #             'Type': type,
# #             'Added On': added_on,
# #             'Furnishing': furnishing,
# #             'Price': price,
# #             'Location': location,
# #             'Bed/Bath/Size': bed_bath_size,
# #             'Permit Number': permit_number,
# #             'Agent Name': agent,
# #             'Primary Image URL': primary_image,
# #             'Breadcrumbs': breadcrumbs,
# #             'Amenities': amenities
# #         }

# #         # Write each property field in column format (column title on the left side) to CSV
# #         for field_name, field_value in property_details.items():
# #             if isinstance(field_value, list):
# #                 field_value = ", ".join(field_value)
# #             self.csv_writer.writerow([field_name, field_value])

# #         # Write property details as JSON entry
# #         json.dump(property_details, self.json_file, ensure_ascii=False, indent=4)

# #         # Add a comma and a newline after each property (except for the last one)
# #         if self.property_count < self.max_properties - 1:
# #             self.json_file.write(',\n')

# #         # Increment the property counter
# #         self.property_count += 1

# #         # Stop the spider once the property limit is reached
# #         if self.property_count >= self.max_properties:
# #             raise CloseSpider(reason="Reached 1500 properties")

# #     def close(self, reason):
# #         """
# #         Close the CSV and JSON files when the spider is finished.
# #         """
# #         # Close the JSON array
# #         self.json_file.write('\n]')
# #         self.json_file.close()

# #         # Close the CSV file
# #         self.csv_file.close()
# import scrapy

# class MyBayutSpider(scrapy.Spider):
#     name = "bayut_spider"
#     allowed_domains = ["www.bayut.com"]
#     start_urls = ["https://www.bayut.com/to-rent/property/dubai/"]

#     def parse(self, response):
#         # Extract property URLs
#         property_urls = response.css('a.d40f2294::attr(href)').getall()  
#         for url in property_urls:
#             yield response.follow(url, self.parse_property)

#         # Extract the URL of the next page using the 'a' tag with title="Next"
#         next_page = response.css('a[title="Next"]::attr(href)').get()

#         # Follow the next page if available
#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse)

#     def parse_property(self, response):
#         # Extract property details
#         price = response.css('span._2d107f6e::text').get().strip()
#         location = response.css('div.e4fd45f0::text').get().strip()
#         bed_bath_size = response.css('span._140e6903::text').get().strip()
#         description_parts = response.css('span._3547dac9::text').getall()
#         description = " ".join([part.strip() for part in description_parts])
#         type = ", ".join(response.css('span._2fdf7fc5[aria-label="Type"]::text').getall())
#         purpose = ", ".join(response.css('span._2fdf7fc5[aria-label="Purpose"]::text').getall())
#         furnishing = ", ".join(response.css('span._2fdf7fc5[aria-label="Furnishing"]::text').getall())
#         added_on = ", ".join(response.css('span._2fdf7fc5[aria-label="Reactivated date"]::text').getall())
#         property_id = ", ".join(response.css('span._2fdf7fc5[aria-label="Reference"]::text').getall())
#         agent = response.css('span._64aa14db a._1264833a::text').getall()
#         permit_number = response.css('span.e56292b8[aria-label="Permit Number"]::text').getall()
#         amenities = response.css('div._1c78af3b + div._117b341a span._7181e5ac::text').getall()
#         amenities = [amenity.strip() for amenity in amenities]
#         breadcrumbs = response.css('div.e28fea44 a._43ad44d9::text').getall()
#         breadcrumbs = [breadcrumb.strip() for breadcrumb in breadcrumbs]

#         # Yield the data you want to save
#         yield {
#             'price': price,
#             'location': location,
#             'bed_bath_size': bed_bath_size,
#             'description': description,
#             'type': type,
#             'purpose': purpose,
#             'furnishing': furnishing,
#             'added_on': added_on,
#             'property_id': property_id,
#             'agent': agent,
#             'permit_number': permit_number,
#             'amenities': amenities,
#             'breadcrumbs': breadcrumbs
#         }
import scrapy
from scrapy.crawler import CrawlerProcess

class MyBayutSpider(scrapy.Spider):
    name = "bayut_spider"
    allowed_domains = ["www.bayut.com"]
    start_urls = ["https://www.bayut.com/to-rent/property/dubai/"]

    # Custom settings for CSV and JSON output
    custom_settings = {
        'FEEDS': {
            'bayut_data.json': {'format': 'json'},
            'bayut_data.csv': {'format': 'csv'},
        },
        'ROBOTSTXT_OBEY': True,  # Make sure you obey robots.txt
    }

    def parse(self, response):
        # Extract product URLs on the current page
        product_urls = response.css('a.d40f2294::attr(href)').getall()
        for url in product_urls:
            yield response.follow(url, self.parse_property)

        # Extract the URL of the next page using the 'a' tag with title="Next"
        next_page = response.css('a[title="Next"]::attr(href)').get()

        # Follow the next page if available
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_property(self, response):
        # Extract data fields, with error handling
        price = response.css('span._2d107f6e::text').get()
        price = price.strip() if price else 'N/A'

        primary_image = response.css('img._4a3dac18::attr(src)').get()
        primary_image = primary_image if primary_image else 'No Image'

        location = response.css('div.e4fd45f0::text').get()
        location = location.strip() if location else 'Unknown Location'

        bed_bath_size = response.css('span._140e6903::text').get()
        bed_bath_size = bed_bath_size.strip() if bed_bath_size else 'Unknown'

        description_parts = response.css('span._3547dac9::text').getall()
        description = " ".join([part.strip() for part in description_parts]) if description_parts else 'No description'

        type = ", ".join(response.css('span._2fdf7fc5[aria-label="Type"]::text').getall()) or 'Unknown Type'
        purpose = ", ".join(response.css('span._2fdf7fc5[aria-label="Purpose"]::text').getall()) or 'Unknown Purpose'
        furnishing = ", ".join(response.css('span._2fdf7fc5[aria-label="Furnishing"]::text').getall()) or 'Unknown Furnishing'
        added_on = ", ".join(response.css('span._2fdf7fc5[aria-label="Reactivated date"]::text').getall()) or 'Unknown Date'
        property_id = ", ".join(response.css('span._2fdf7fc5[aria-label="Reference"]::text').getall()) or 'Unknown Property ID'

        agent = response.css('span._64aa14db a._1264833a::text').getall() or response.css('span._4c376836 undefined a.d2d04ff3::text').getall()
        agent = [name.strip() for name in agent if name.strip()] or ['No Agent']

        permit_number = response.css('span.e56292b8[aria-label="Permit Number"]::text').getall() or ['Unknown Permit Number']
        amenities = response.css('div._1c78af3b + div._117b341a span._7181e5ac::text').getall() or ['No Amenities']
        breadcrumbs = response.css('div.e28fea44 a._43ad44d9::text').getall() or ['No Breadcrumbs']

        # Yield the data as a dictionary (this will save to JSON and CSV)
        yield {
            'price': price,
            'primary_image': primary_image,
            'location': location,
            'bed_bath_size': bed_bath_size,
            'description': description,
            'type': type,
            'purpose': purpose,
            'furnishing': furnishing,
            'added_on': added_on,
            'property_id': property_id,
            'agent': agent,
            'permit_number': permit_number,
            'amenities': amenities,
            'breadcrumbs': breadcrumbs
        }

# Run the spider
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(MyBayutSpider)
    process.start()