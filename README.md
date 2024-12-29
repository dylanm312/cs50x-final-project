# Vehicle Maintenance Tracker
### Video Demo: https://youtu.be/ib73li3Dj8M
### Description: This project is a vehicle maintenance tracker, designed to help individuals or corporations manage the maintenance schedules of their vehicles. The application is written in Python using Django for the MVC stack, and Bootstrap for the front-end aesthetics.

## Project Overview

The Vehicle Maintenance Tracker is a tool designed to keep track of maintenance tasks for personal or corporate vehicles. It allows users to log maintenance activities and view the history of services performed on each vehicle.

## Models / Data Structure

There are three models in this project:

1. Vehicle - A Vehicle object represents a motor vehicle. This can be a car, motorcycle, boat, airplane, lawnmower, etc. It is an object which Maintenance Events are logged against.

2. Maintenance Item - A Maintenance Item describes a generic action that could be performed on a vehicle. These includes such items as an Oil Change, Brake Service, or Tire Rotation. They represent the scope of a maintenance item, but not any specific instance of maintenance on a particular vehicle. That is represented by a Vehicle Event

3. Vehicle Event - A Vehicle Event represents a discrete instance of a Maintenance Item. In other words, after adding a date, vehicle ID, vehicle mileage, and timestamp to a Maintenance Item, we can create a Vehicle Event. Vehicle Events can also be created without being connected to a Maintenance Item. This can be useful for tracking mileages for road trips, monitoring fuel and toll spend for fleets, and/or other miscellaneous purposes.

These models (including their schemas and data) are stored in an SQLite database (db.sqlite3), which can be found in the root project directory.

## Request Flows

When the user first loads the homepage at http://localhost:8000, an HTTP GET request is sent to the Django development server (which is launched by running `python manage.py runserver` in the project root directory). This HTTP request flows through the top-level `urls.py` routing file, where Django attempts to match the requested URL with a `urlpattern` described in the routing file. The root URL (`/`) is mapped to the app-level routing file located at `ui/urls.py`, so the matched part of the URL (in this case, just the leading `/`) is truncated from the beginning of the request URL, and the remainder is sent forward to the app-level `urls.py` file.

The app-level routing file functions identically to the top/project-level routing file, except this one is more interesting and contains most of the URLs for the project. Here we can see various URLs to create/edit/delete the various models involved in this project. After matching against a URL pattern, the request is forwarded to the appropriate `view` (defined in `ui/views.py`) which is where the database lookups and other application logic takes place. After completing various different types of request processing, the view handler then invokes the Django template rendering engine known as Jinja. The appropriate template from `ui/templates/ui` is imported, parsed, and returned as an HttpResponse back to the user's original HttpRequest. This completes the application workflow for a request. GET and POST requests are both processed in the same way, though they are often routed to different views to be handled accordingly.

## Features

- **Add Vehicles**: Users can add multiple vehicles to the tracker.
- **Log Maintenance**: Record details of maintenance activities performed.
- **View History**: Access a log of all maintenance activities for each vehicle.

### Add Vehicles

On the homepage, users can add vehicles to the system by clicking the "+Add" button. A form appears (vehicle_form.html), prompting the user to fill in information about their vehicle. Upon successfully completing the form, the user is returned to the homepage, where a toast appears at the top to indicate that the action was performed successfully. This toast system uses Django's "messages" middleware and is used throughout the project to inform the user of the outcomes of their attempted actions.

### Log Maintenance

After creating a vehicle, users can click on their new vehicle's name on the homepage to go to that vehicle's Vehicle Detail page (vehicle_detail.html). This page shows the details of the selected vehicle (such as year, make, model, color, etc) in read-only format, along with a table of Vehicle Events below it. Users can add new Vehicle Events here by clicking the "+Add Vehicle Event" button. A form system similar to that used during vehicle creation is provided for the purpose of adding or editing Vehicle Events.

New Vehicle Events created in the UI are automatically linked via a ForeignKey relationship to the Vehicle corresponding to the Vehicle Detail page from which they were created.

### View History

On the Vehicle Detail page, users can view, edit, and delete Vehicle Events from a Vehicle's history. This is useful for understanding what events (maintenance or otherwise) have occurred to a vehicle in its history, and for editing or removing mistakes in the vehicle's record.

## Admin Site

One obvious feature is missing from the user interface - there is no way to create, edit, or delete Maintenance Items from the system. This is considered an administrative task, so it is only possible via the Django admin interface (located at http://localhost:8000/admin). The default login for this admin user is root:root (that is, a username of `root` and a password of `root`). This is obviously not very secure at all, but is adequate for demonstration purposes.

Once logged into the admin interface, an administrator can perform all of the same functions an end user can perform from the normal homepage, as well as the administration of Maintenance Items. The interface for creating, editing, and deleting model instances here is self-explanatory. One detail to note is that when editing a Vehicle in the admin view, the associated Vehicle Events appear below it, allowing for easier Vehicle and Vehicle Event editing all in one place. This is accomplished through the use of custom AdminInterface and TabularInline classes, which are defined in the `ui/admin.py` file.