from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.Views import User, RealEstate
from authentication.Views import Login

urlpatterns = [
    # JWT Authentication
    path('authenticate', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # User Management
    path('users', User.UserView.as_view(), name="UserView"),
    path('users/<int:pk>', User.UserDetailView.as_view(), name="UserDetailView"),

    # path('login', Login.LoginView.as_view({'post': 'login'})),
    # path('logout', Login.LogoutView.as_view({'post': 'logout'})),


    #Realstate
    path('real_estate', RealEstate.RealEstateView.as_view(), name="RealEstateView"),
    path('real_estate/<int:pk>', RealEstate.RealEstateDetailView.as_view(), name="RealEstateDetailView"),

    # user all listings
    path('user_listings', RealEstate.UserRealEstateListingView.as_view(), name="UserRealEstateListingView"),

]
