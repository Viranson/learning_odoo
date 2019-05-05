from odoo.tests import common

class test_project(common.TransactionCase):
    
    def test_create_data(self):
        
        i = 0
        while i <= 5 :
            
            vals_project = {}
            
            
            
            vals_project['name'] = 'Project %s'%(str(i))
            test_project = self.env['project.project'].create(vals_project)
            self.assertEqual(test_project.name, vals_project['name'])
            
            j = 0
            while j < 5 :
                
                vals_task = {}
                vals_task['name'] = "task %s"%(str(j))
                vals_task['project_id'] = test_project.id
                test_task = self.env['project.task'].create(vals_task)
                
                self.assertEqual(test_task.name, vals_task['name'])
                self.assertEqual(test_task.project_id.id, "asdas")
                j = j + 1

            i = i + 1
            
        print "Congratulation, your test was successful. Great Job dude !!! "