# 🔧 Formatter System

A comprehensive Python system for processing and formatting nested class data, providing multiple levels of field access and formatting capabilities through three specialized modules.

## 📦 Modules

### [Get All Model Fields](./get-all-model-fields/)

The foundation module that provides basic field retrieval functionality:

- Automatic field discovery and extraction
- Complete class hierarchy traversal
- Basic value retrieval without formatting

### [Models Specific Fields](./models-specific-fields/)

Builds upon the base module to add selective field access:

- Targeted field retrieval using predefined paths
- Field mapping and type conversion support
- Enhanced field access patterns

### [Models With Formatter](./models-with-formatter/)

The most advanced module offering comprehensive formatting capabilities:

- Configurable field formatting with prefix/suffix
- Custom delimiter configuration
- Multiple formatter profiles support

## 📊 Class Structure

All modules work with the same base class hierarchy:

```
Class_A
├── class_b (Class_B)
│   ├── class_c (Class_C)
│   │   └── class_e (Class_E)
│   └── class_d[] (Array of Class_D)
│       └── class_e (Class_E)
```

## License

This project is licensed under the MIT License.
