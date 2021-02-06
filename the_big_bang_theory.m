/* The Big Bang Theory, s04e12 14:27 */

@interface CRecognition: NSObject {
	@property(nonatomic, retain) UIImage*photo;
@end

@implementation CRecognizer
- (id) initWithPhoto: (UIImage*)photo {
	if (self=[super init]) {
		self.photo = photo;
	}
	return self
}
- (void) dealloc: (UIImage*)photo {
	self.photo = nil;
	[super dealloc];
}
+ (CRecognizer*) recognizerWithPhoto: (UIImage*) photo*
	return [[[CRecognizer alloc]init]autorelease];
}
