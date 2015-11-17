replacement:

deleted:

		2

replaced by:

		3

reason: ()

deleted:

		3

replaced by:

		4

reason: ()

deleted:

		4

replaced by:

		5

reason: ()

deleted:

		5

replaced by:

		6

reason: ()

deleted:

		// Get the logged-in user.
			                var currentUser = context.Principal as ServiceUser;
			
			                // Add a new tag that is the user ID.
			                registration.Tags.Add(currentUser.Id);
			
			                services.Log.Info("Registered tag for userId: " + currentUser.Id);
			            }
			            catch(Exception ex)
			            {
			                services.Log.Error(ex.ToString());
			            }
			                return Task.FromResult(true);
			        }
			
			        private bool ValidateTags(NotificationRegistration registration)
			        {
			            // Create a regex to search for disallowed tags.
			            System.Text.RegularExpressions.Regex searchTerm =
			            new System.Text.RegularExpressions.Regex(@"facebook:|google:|twitter:|microsoftaccount:",
			                System.Text.RegularExpressions.RegexOptions.IgnoreCase);
			
			            foreach (string tag in registration.Tags)
			            {
			                if (searchTerm.IsMatch(tag))
			                {
			                    return false;
			                }
			            }
			            return true;
			        }
				
			        public Task Unregister(ApiServices services, HttpRequestContext context,

replaced by:

		// Get the logged-in user.
		                var currentUser = context.Principal as ServiceUser;
		
		                // Add a new tag that is the user ID.
		                registration.Tags.Add(currentUser.Id);
		
		                services.Log.Info("Registered tag for userId: " + currentUser.Id);
		            }
		            catch(Exception ex)
		            {
		                services.Log.Error(ex.ToString());
		            }
		                return Task.FromResult(true);
		        }
		
		        private bool ValidateTags(NotificationRegistration registration)
		        {
		            // Create a regex to search for disallowed tags.
		            System.Text.RegularExpressions.Regex searchTerm =
		            new System.Text.RegularExpressions.Regex(@"microsoftaccount:",
		                System.Text.RegularExpressions.RegexOptions.IgnoreCase);
		
		            foreach (string tag in registration.Tags)
		            {
		                if (searchTerm.IsMatch(tag))
		                {
		                    return false;
		                }
		            }
		            return true;
		        }
			
		        public Task Unregister(ApiServices services, HttpRequestContext context,

reason: ()

deleted:

		6

replaced by:

		7

reason: ()

deleted:

		7

replaced by:

		8

reason: ()

