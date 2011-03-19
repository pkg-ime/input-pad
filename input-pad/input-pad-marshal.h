
#ifndef __INPUT_PAD_MARSHAL_H__
#define __INPUT_PAD_MARSHAL_H__

#include	<glib-object.h>

G_BEGIN_DECLS

/* BOOL:STRING,UINT,UINT,UINT,UINT (input-pad-marshal.list:1) */
extern void INPUT_PAD_BOOLEAN__STRING_UINT_UINT_UINT_UINT (GClosure     *closure,
                                                           GValue       *return_value,
                                                           guint         n_param_values,
                                                           const GValue *param_values,
                                                           gpointer      invocation_hint,
                                                           gpointer      marshal_data);
#define INPUT_PAD_BOOL__STRING_UINT_UINT_UINT_UINT	INPUT_PAD_BOOLEAN__STRING_UINT_UINT_UINT_UINT

/* VOID:STRING,STRING (input-pad-marshal.list:2) */
extern void INPUT_PAD_VOID__STRING_STRING (GClosure     *closure,
                                           GValue       *return_value,
                                           guint         n_param_values,
                                           const GValue *param_values,
                                           gpointer      invocation_hint,
                                           gpointer      marshal_data);

/* VOID:OBJECT,OBJECT (input-pad-marshal.list:3) */
extern void INPUT_PAD_VOID__OBJECT_OBJECT (GClosure     *closure,
                                           GValue       *return_value,
                                           guint         n_param_values,
                                           const GValue *param_values,
                                           gpointer      invocation_hint,
                                           gpointer      marshal_data);

G_END_DECLS

#endif /* __INPUT_PAD_MARSHAL_H__ */

