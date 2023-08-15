from datapackage import Package

package = Package()
package.infer('archive/car_models.csv')
package.infer('data/csv.csv')
package.infer('data/expandeds.csv')
package.commit()
package.save('datapackage.json')