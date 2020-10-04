from OllinCafeManagement.database import cursor

class UserPermissionView():

    def get_user(request, user_id):
        cursor.execute("SELECT core_staff.staff_id,  core_staff.staff_name, core_staff.profile_image, core_storestaffdetail.store_id, auth_user_groups.group_id "+
                        "FROM core_staff, auth_user, auth_user_groups, core_storestaffdetail "+
                        "WHERE core_storestaffdetail.staff_id = core_staff.staff_id AND auth_user_groups.user_id = core_staff.user_id AND core_staff.user_id = %s" , (user_id, ))
        user_info = cursor.fetchone()
        if not user_info:
            request.session['permission'] = 0
        else:
            request.session['user_id'] = str(user_info[0])
            request.session['user_name'] = str(user_info[1])
            request.session['profile_image'] = str(user_info[2])
            request.session['store'] = str(user_info[3])
            request.session['permission'] = str(user_info[4])

    def get_store(request, user_id):
        cursor.execute("SELECT core_store.store_name " + 
                       "FROM core_store, core_staff, core_storestaffdetail, auth_user " +
                       "WHERE core_staff.staff_id = core_storestaffdetail.staff_id " +
                       "AND core_storestaffdetail.store_id = core_store.store_id " +
                       "AND core_staff.user_id =%s GROUP BY core_store.store_name " , (user_id, ))
        user_store = cursor.fetchall()
        print(user_store)
        for item in user_store:
            print(item[0])
        return user_store